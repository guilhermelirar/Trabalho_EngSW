# app/models/project.py
from app.models import db

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    owner_id = db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable=False)

    backlog = db.relationship(
        'ProjectBacklog',
        back_populates='project',
        uselist=False,
        cascade='all, delete-orphan',
    )
