import pytest
from flask import Flask

from app.services import user_story_service


def test_create_user_story_success(app: Flask, project_with_backlog, test_user):
    """
    Cria história de usuário para um projeto com backlog existente
    """
    with app.app_context():
        story_data = {
            "title": "Criar História",
            "role": "Desenvolvedor",
            "action": "Criar uma US",
            "benefit": "Organizar o backlog",
        }

        story = user_story_service.create_user_story(
            project_id=project_with_backlog.id,
            user_id=test_user.id,
            data=story_data,
        )

        assert story.id is not None
        assert story.title == "Criar História"
        assert story.project_backlog_id == project_with_backlog.backlog.id
