import pytest
from flask import Flask
from sqlalchemy.sql.operators import ne

from app.services import user_story_service
from app.services.exceptions import ProjectDomainException, UserStoryDomainException


def story_data() -> dict:
    return {
        "title": "Criar História",
        "role": "Desenvolvedor",
        "action": "Criar uma US",
        "benefit": "Organizar o backlog",
    }


def test_create_user_story_success(app: Flask, project_with_backlog, test_user):
    """
    Cria história de usuário para um projeto com backlog existente
    """
    with app.app_context():
        story = user_story_service.create_user_story(
            project_id=project_with_backlog.id,
            user_id=test_user.id,
            data=story_data(),
        )

        assert story.id is not None
        assert story.title == "Criar História"
        assert story.project_backlog_id == project_with_backlog.backlog.id


def test_update_user_story_success(app: Flask, project_with_backlog, test_user):
    """
    Atualiza história de usuário para um projeto com backlog existente
    """
    with app.app_context():
        data = story_data()
        story = user_story_service.create_user_story(
            project_id=project_with_backlog.id,
            user_id=test_user.id,
            data=data,
        )

        old_title = story.title
        new_data = {"title": "New" + data["title"]}

        new_story = user_story_service.update_user_story(
            story.id, test_user.id, new_data
        )

        assert new_story.title != old_title


def test_create_user_story_handles_permission(
    app: Flask, project_with_backlog, test_user
):
    """
    Cria história de usuário para um projeto com backlog existente, mas usuário
    não é dono do projeto
    """
    with (
        app.app_context(),
        pytest.raises(ProjectDomainException, match="Projeto não encontrado"),
    ):
        user_story_service.create_user_story(
            project_id=project_with_backlog.id,
            user_id=test_user.id + 1,
            data=story_data(),
        )


def test_delete_user_story_success(app: Flask, project_with_backlog, test_user):
    """
    Deleta uma história de usuário existente e confirma que ela não é mais encontrada.
    """
    with app.app_context():
        # Arrange: Cria a história de usuário que será deletada
        story = user_story_service.create_user_story(
            project_id=project_with_backlog.id,
            user_id=test_user.id,
            data=story_data(),
        )
        story_id = story.id

        # Act: executa a deleção
        user_story_service.delete_user_story(
            story_id=story_id, project_id=project_with_backlog.id, user_id=test_user.id
        )

        # Assert: valida que buscar a história deletada lança UserStoryDomainException (404)
        with pytest.raises(UserStoryDomainException) as exc_info:
            user_story_service.get_user_story(
                story_id=story_id,
                project_id=project_with_backlog.id,
                user_id=test_user.id,
            )

        assert exc_info.value.status_code == 404
