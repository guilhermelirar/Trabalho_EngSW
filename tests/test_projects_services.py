import pytest
from flask import Flask
from typing_extensions import get_protocol_members

from app.services.auth_service import register_user
from app.services.project_service import *


def get_valid_user_id(name="user"):
    return register_user(name, f"{name}@email.com", "password123").id


def test_project_creation_success(app: Flask):
    # US-005 criação de projetos bem sucedida
    with app.app_context():
        user_id = get_valid_user_id()
        proj = create_project(user_id, "Project 1")

        assert proj is not None
        assert proj.owner_id == user_id


def test_project_read_list_success(app: Flask):
    # US-005 listagem de projetos criados bem sucedida
    with app.app_context():
        user_id = get_valid_user_id()
        projects_before = get_projects_by_user(user_id)

        for i in range(10):
            create_project(user_id, f"Project {i}")

        projects_after = get_projects_by_user(user_id)

        assert projects_before == []
        assert len(projects_after) == 10


def test_project_delete_success(app: Flask):
    # US-005 exclusão de projeto é bem sucedida
    with app.app_context():
        user_id = get_valid_user_id()

        project_id = create_project(user_id, f"Project").id
        delete_project(project_id, user_id)

        assert get_projects_by_user(user_id) == []


def test_project_delete_handles_permission(app: Flask):
    # US-005 exclusão de projeto levanta exceção em caso de
    # projeto não pertencer ao usuário
    with app.app_context():
        user_id = get_valid_user_id()
        project_id = create_project(user_id, "Project").id

        with pytest.raises(ProjectDomainException, match="Projeto não encontrado"):
            delete_project(project_id, user_id + 1)
            assert get_projects_by_user(user_id) != []


def test_project_read_handles_permission(app: Flask):
    # US-005 projeto não encontrado caso não pertença ao usuário
    with app.app_context():
        user_id = get_valid_user_id()
        project_id = create_project(user_id, "Project").id

        with pytest.raises(ProjectDomainException, match="Projeto não encontrado"):
            get_project_by_id(project_id, user_id + 1)


def test_project_read_details_success(app: Flask):
    # US-005 projeto encontrado e com detalhes
    with app.app_context():
        user_id = get_valid_user_id()
        project_id = create_project(user_id, "Project").id

        project = get_project_by_id(project_id, user_id)
        assert project.id == project_id
        assert project.name == "Project"
        assert not project.backlog  # backlog não criado


def test_update_project_success(app: Flask):
    # US-005 projeto encontrado e com detalhes
    with app.app_context():
        user_id = get_valid_user_id()
        project_id = create_project(user_id, "Project").id

        just_updated = update_project(project_id, user_id, name="Updated Project")
        get_updated = get_project_by_id(project_id, user_id)

        assert just_updated.name == "Updated Project"
        assert just_updated.id == get_updated.id
        assert just_updated.name == get_updated.name


def test_create_backlog_success(app: Flask):
    # US-006 criação de product backlog
    with (
        app.app_context(),
        pytest.raises(
            ProjectDomainException, match="Backlog já existe para este projeto"
        ),
    ):
        user_id = get_valid_user_id()
        project_id = create_project(user_id, "Project").id
        backlog = create_product_backlog(project_id, user_id)

        assert backlog is not None
        create_product_backlog(project_id, user_id)  # Criando quando já existe


def test_delete_backlog_success(app: Flask):
    # US-006 deletar product backlog
    with app.app_context():
        user_id = get_valid_user_id()
        project = create_project(user_id, "Project")

        db.session.refresh(project)

        delete_product_backlog(project.id, user_id)  # não deve lançar erro
        create_product_backlog(project.id, user_id)  # cria um backlog
        delete_product_backlog(project.id, user_id)  # deleta
        assert project.backlog is not None
