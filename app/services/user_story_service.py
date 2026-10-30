from app.models import db
from app.models.user_story import UserStory
from app.services import project_service
from app.services.exceptions import ProjectDomainException, UserStoryDomainException


def validate_user_story_data(data: dict, require_all: bool = True) -> None:
    required_fields = ["title", "role", "action", "benefit"]
    for field in required_fields:
        val = data.get(field)
        if (not val and require_all) or not str(val).strip():
            raise UserStoryDomainException(f"O campo '{field}' é obrigatório.")


def create_user_story(project_id: int, user_id: int, data: dict) -> UserStory:
    """
    Cria uma história de usuário associada a um projeto
    """
    # Valida se projeto pertence ao usuário
    project = project_service.get_project_by_id(project_id, user_id)
    if not project:
        raise ProjectDomainException("Projeto não encontrado", status_code=404)
    if not project.backlog:
        raise ProjectDomainException(
            "O projeto não possui um Product Backlog.", status_code=404
        )

    validate_user_story_data(data, require_all=True)

    user_story = UserStory()
    user_story.project_backlog_id = project.backlog.id
    user_story.title = str(data["title"]).strip()
    user_story.role = str(data["role"]).strip()
    user_story.action = str(data["action"]).strip()
    user_story.benefit = str(data["benefit"]).strip()

    db.session.add(user_story)
    db.session.commit()
    return user_story


def update_user_story(story_id: int, user_id: int, new_data: dict) -> UserStory:
    """
    Edita campos de uma história de usuário existente.
    """
    # busca história de usuário no banco de dados
    story = UserStory.query.get(story_id)
    if not story:
        raise UserStoryDomainException(
            "História de usuário não encontrada.", status_code=404
        )

    if not project_service.get_project_by_id(story.project_backlog.project_id, user_id):
        raise ProjectDomainException("Projeto não encontrado", status_code=404)

    validate_user_story_data(new_data, require_all=False)
    story.title = str(new_data["title"]).strip()
    story.role = str(new_data["role"]).strip()
    story.action = str(new_data["action"]).strip()
    story.benefit = str(new_data["benefit"]).strip()

    db.session.commit()
    return story
