# Modelo para uma história de usuário
from app.models import db

class UserStory(db.Model):
    __tablename__ = 'user_stories'

    id = db.Column(db.Integer, primary_key=True)
    project_backlog_id = db.Column(
        db.Integer,
        db.ForeignKey('project_backlogs.id'),
        nullable=False,
    )
    sprint_backlog_id = db.Column(
        db.Integer,
        db.ForeignKey('sprint_backlogs.id'),
        nullable=True,
    )
    title = db.Column(db.Text, nullable=False)
    role = db.Column(db.Text, nullable=False)
    action = db.Column(db.Text, nullable=False)
    benefit = db.Column(db.Text, nullable=False)

    project_backlog = db.relationship('ProjectBacklog', back_populates='user_stories')
    sprint_backlog = db.relationship('SprintBacklog', back_populates='user_stories')
