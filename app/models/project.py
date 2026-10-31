from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from app.models import db

if TYPE_CHECKING:
    from app.models.project_backlog import ProjectBacklog


class Project(db.Model):
    __tablename__ = "projects"

    id: Mapped[int] = db.Column(db.Integer, primary_key=True)
    name: Mapped[str] = db.Column(db.Text, nullable=False)
    description: Mapped[str | None] = db.Column(db.Text, nullable=True)
    owner_id: Mapped[int] = db.Column(
        "user_id", db.Integer, db.ForeignKey("users.id"), nullable=False
    )

    backlog: Mapped["ProjectBacklog | None"] = relationship(
        "ProjectBacklog",
        back_populates="project",
        uselist=False,
        cascade="all, delete-orphan",
    )
