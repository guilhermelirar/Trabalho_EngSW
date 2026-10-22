# app/models/init.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.models.user import User
from app.models.project import Project
from app.models.project_backlog import ProjectBacklog
from app.models.sprint import Sprint, SprintBacklog
from app.models.user_story import UserStory
