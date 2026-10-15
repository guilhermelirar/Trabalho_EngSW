# app/models/init.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# models/__init__.py
from app.models.User import User
