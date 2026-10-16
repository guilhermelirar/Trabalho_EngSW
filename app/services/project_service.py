# app/services/project_service.py
# Camada de negócios para gerenciamento de Projetos

from typing import Sequence

from app.models.project import Project
from app.services.auth_service import get_user_by_id
from app.models import db
from app.services.exceptions import ProjectDomainException

from sqlalchemy import select

def validate_user_id(user_id: int):
    user = get_user_by_id(user_id)
    if user is None:
        raise ProjectDomainException("Usuário responsável não foi encontrado.")
    return user

def create_project(user_id: int, name: str) -> Project:
    validate_user_id(user_id)
    name = name.strip()
    
    if not name:
        raise ProjectDomainException("O nome do projeto não pode ser vazio.")
        
    if len(name) > 100:
        raise ProjectDomainException("O nome do projeto não pode conter mais de 100 caracteres.")

    project = Project()
    project.name = name
    project.owner_id = user_id

    db.session.add(project)
    db.session.commit()
    return project

def get_projects_by_user(user_id: int) -> Sequence[Project]:
    validate_user_id(user_id)
    query = select(Project).where(Project.owner_id == user_id)
    return db.session.scalars(query).all()

