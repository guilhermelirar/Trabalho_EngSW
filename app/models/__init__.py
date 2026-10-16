# app/models/init.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from app.models.user import User
from app.models.project import Project
from app.models.sprint import Sprint
