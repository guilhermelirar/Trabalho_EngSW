from flask import Flask

from app.services.auth_service import register_user
from app.services.project_service import *

def get_valid_user_id():
    return register_user("user", "user@email.com", "password123").id

def test_project_creation_success(app: Flask):
    # US-005 criação de projetos bem sucedida
    with app.app_context():
        user_id = get_valid_user_id()
        proj = create_project(user_id, "Project 1")
        
        assert proj is not None
        assert proj.owner_id == user_id

def test_project_read_success(app: Flask):
    # US-005 listagem de projetos criados bem sucedida
    with app.app_context():
        user_id = get_valid_user_id()
        projects_before = get_projects_by_user(user_id)

        for i in range(10):
            create_project(user_id, f"Project {i}")

        projects_after = get_projects_by_user(user_id)

        assert projects_before == []
        assert len(projects_after) == 10 

