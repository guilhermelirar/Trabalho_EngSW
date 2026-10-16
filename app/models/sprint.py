# Modelo para uma SprintBacklog
from app.models import db

class Sprint(db.Model):
    __tablename__ = 'sprints'
    id = db.Column(db.Integer, primary_key = True)
    project_id = db.Column(db.Integer, 
                           db.ForeignKey('projects.id'), 
                           nullable=False)

