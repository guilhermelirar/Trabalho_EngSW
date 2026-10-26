from sqlalchemy.orm import relationship
from sqlalchemy.orm.base import Mapped

from app.models import db
from app.models.project import Project
from app.models.sprint import SprintBacklog
from app.models.user_story import UserStory


class ProjectBacklog(db.Model):
    __tablename__ = "project_backlogs"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(
        db.Integer,
        db.ForeignKey("projects.id"),
        nullable=False,
        unique=True,
    )

    project: Mapped["Project"] = relationship("Project", back_populates="backlog")

    sprints: Mapped["SprintBacklog"] = relationship(
        "SprintBacklog",
        back_populates="project_backlog",
        cascade="all, delete-orphan",
        uselist=False,
    )

    user_stories: Mapped["UserStory"] = relationship(
        "UserStory",
        back_populates="project_backlog",
        cascade="all, delete-orphan",
        uselist=False,
    )
