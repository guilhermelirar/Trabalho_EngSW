# app/services/project_service.py
# Camada de negócios para gerenciamento de Projetos

from collections.abc import Sequence

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from app.models import db
from app.models.project import Project
from app.models.project_backlog import ProjectBacklog
from app.services.auth_service import get_user_by_id
from app.services.exceptions import ProjectDomainException


def validate_user_id(user_id: int):
    user = get_user_by_id(user_id)
    if user is None:
        raise ProjectDomainException("Usuário responsável não foi encontrado.")
    return user


def validate_project_name(name: str | None):
    if not name:
        raise ProjectDomainException("O nome do projeto não pode ser vazio.")

    clean_name = name.strip()

    if len(clean_name) > 100:
        raise ProjectDomainException(
            "O nome do projeto não pode conter mais de 100 caracteres."
        )

    return clean_name


def create_project(user_id: int, name: str | None) -> Project:
    """
    (US005 Create)
    Criar projeto de nome 'name' associado a um usuário com id 'user_id'.
    Retorna o projeto em caso de sucesso, ou lança exceção ProjectDomainException
    em caso de erro de validação
    """
    validate_user_id(user_id)
    clean_name = validate_project_name(name)

    project = Project()
    project.name = clean_name
    project.owner_id = user_id

    db.session.add(project)
    db.session.commit()
    return project


def get_projects_by_user(user_id: int) -> Sequence[Project]:
    """
    (US005 Read)
    Retorna iterável Sequence[Project] com a lista de projetos
    associados ao usuário de id 'user_id'
    """
    validate_user_id(user_id)
    query = select(Project).where(Project.owner_id == user_id)
    return db.session.scalars(query).all()


def delete_project(project_id: int, owner_id: int):
    """
    (US005 DELETE)
    Deleta um projeto de id 'project_id' associado a um
    dono 'owner_id'. Em caso de não encontrado, irá levantar
    uma exceção ProjectDomainException
    """
    project = db.session.get(Project, project_id)

    if project and project.owner_id == owner_id:
        db.session.delete(project)
        db.session.commit()
        return

    raise ProjectDomainException("Projeto não encontrado", status_code=404)


def get_project_by_id(project_id: int, owner_id: int):
    """
    (US005 READ)
    Obtém projeto com campos nome, descrição, e lista de histórias
    de usuário (project backlog)
    """
    project = (
        Project.query.options(
            joinedload(Project.backlog).joinedload(ProjectBacklog.user_stories),
            joinedload(Project.backlog).joinedload(ProjectBacklog.sprints),
        )
        .filter_by(id=project_id, owner_id=owner_id)
        .first()
    )

    if project:
        return project

    raise ProjectDomainException("Projeto não encontrado", status_code=404)


def update_project(project_id: int, owner_id: int, name: str) -> Project:
    """
    (US005 Update)
    Atualiza campos do projeto (nome)
    """
    new_name = validate_project_name(name)
    project = db.session.get(Project, project_id)

    # Se existe e é do usuário, atualizar e retornar
    if project and project.owner_id == owner_id:
        project.name = new_name
        db.session.commit()
        return project

    raise ProjectDomainException("Projeto não encontrado", status_code=404)
