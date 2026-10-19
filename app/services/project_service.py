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
    """
    Criar projeto de nome 'name' associado a um usuário com id 'user_id'.
    Retorna o projeto em caso de sucesso, ou lança exceção ProjectDomainException
    em caso de erro de validação
    """
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
    """
    Retorna iterável Sequence[Project] com a lista de projetos 
    associados ao usuário de id 'user_id'
    """
    validate_user_id(user_id)
    query = select(Project).where(Project.owner_id == user_id)
    return db.session.scalars(query).all()

def delete_project(project_id: int, owner_id: int):
    """
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
