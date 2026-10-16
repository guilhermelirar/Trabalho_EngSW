from flask import Flask

from app.services.auth_service import register_user
from app.services.project_service import *

def get_valid_user_id():
    return register_user("user", "user@email.com", "password123").id

def test_project_creation_success(app: Flask):
    with app.app_context():
        user_id = get_valid_user_id()
        proj = create_project(user_id, "Project 1")
        
        assert proj is not None
        assert proj.owner_id == user_id
