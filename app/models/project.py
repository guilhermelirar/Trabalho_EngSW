# app/models/project.py
from app.models import db

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relacionamentos
    sprints = db.relationship('Sprint', backref='project', 
                              lazy=True, cascade="all, delete-orphan")
