# Modelo para uma sprint do backlog
from app.models import db


class SprintBacklog(db.Model):
    __tablename__ = "sprint_backlogs"

    id = db.Column(db.Integer, primary_key=True)
    project_backlog_id = db.Column(
        db.Integer,
        db.ForeignKey("project_backlogs.id"),
        nullable=False,
    )
    sprint_number = db.Column(db.Integer, nullable=False)
    __table_args__ = (
        db.UniqueConstraint(
            "project_backlog_id",
            "sprint_number",
            name="uq_sprint_backlog_number",
        ),
    )

    project_backlog = db.relationship("ProjectBacklog", back_populates="sprints")
    user_stories = db.relationship("UserStory", back_populates="sprint_backlog")


Sprint = SprintBacklog
