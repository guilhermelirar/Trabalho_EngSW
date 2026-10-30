from sqlalchemy.orm import Mapped, relationship

from app.models import db


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

    sprints: Mapped[list["SprintBacklog"]] = relationship(
        "SprintBacklog",
        back_populates="project_backlog",
        cascade="all, delete-orphan",
    )

    user_stories: Mapped[list["UserStory"]] = relationship(
        "UserStory",
        back_populates="project_backlog",
        cascade="all, delete-orphan",
    )
