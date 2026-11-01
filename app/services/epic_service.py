"""Regras de negócio para os épicos de um Product Backlog."""

from app.models import db
from app.models.epic import Epic
from app.services import project_service
from app.services.exceptions import ProjectDomainException, ServiceException
from app.services.user_story_service import get_user_story


class EpicDomainException(ServiceException):
    """Erros relacionados ao gerenciamento de épicos."""


def validate_epic_title(title: str | None) -> str:
    if not title or not title.strip():
        raise EpicDomainException("O título do épico é obrigatório.")

    clean_title = title.strip()
    if len(clean_title) > 120:
        raise EpicDomainException("O título do épico pode ter no máximo 120 caracteres.")
    return clean_title


def get_epic(epic_id: int, project_id: int, user_id: int) -> Epic:
    project = project_service.get_project_by_id(project_id, user_id)
    if not project.backlog:
        raise ProjectDomainException("O projeto não possui um Product Backlog.")

    epic = db.session.get(Epic, epic_id)
    if not epic or epic.project_backlog_id != project.backlog.id:
        raise EpicDomainException("Épico não encontrado.", status_code=404)
    return epic


def create_epic(project_id: int, user_id: int, title: str | None) -> Epic:
    project = project_service.get_project_by_id(project_id, user_id)
    if not project.backlog:
        raise ProjectDomainException("Crie o Product Backlog antes de adicionar um épico.")

    epic = Epic()
    epic.project_backlog_id = project.backlog.id
    epic.title = validate_epic_title(title)
    db.session.add(epic)
    db.session.commit()
    return epic


def update_epic(
    epic_id: int, project_id: int, user_id: int, title: str | None
) -> Epic:
    epic = get_epic(epic_id, project_id, user_id)
    epic.title = validate_epic_title(title)
    db.session.commit()
    return epic


def delete_epic(epic_id: int, project_id: int, user_id: int) -> None:
    epic = get_epic(epic_id, project_id, user_id)

    # O épico é apenas uma organização das HUs; excluí-lo não exclui requisitos.
    for story in epic.user_stories:
        story.epic_id = None
    db.session.delete(epic)
    db.session.commit()


def link_user_story(epic_id: int, story_id: int, project_id: int, user_id: int) -> None:
    epic = get_epic(epic_id, project_id, user_id)
    story = get_user_story(story_id, project_id, user_id)
    story.epic_id = epic.id
    db.session.commit()


def unlink_user_story(epic_id: int, story_id: int, project_id: int, user_id: int) -> None:
    epic = get_epic(epic_id, project_id, user_id)
    story = get_user_story(story_id, project_id, user_id)
    if story.epic_id != epic.id:
        raise EpicDomainException("A história não está vinculada a este épico.")
    story.epic_id = None
    db.session.commit()
