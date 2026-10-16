# Modelo para uma história de usuário
from app.models import db

class UserStory(db.Model):
    __tablename__ = 'user_stories'
    id = db.Column(db.Integer, primary_key = True)
