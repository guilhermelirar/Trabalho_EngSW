# Modelo para uma história de usuário
from app.models import db

class UserStory(db.Model):
    __tablename__ = "user_stories"

    id = db.Column(db.Integer, primary_key=True)
    project_backlog_id = db.Column(
        db.Integer,
        db.ForeignKey("project_backlogs.id"),
        nullable=False,
    )
    sprint_backlog_id = db.Column(
        db.Integer,
        db.ForeignKey("sprint_backlogs.id"),
    )
    epic_id = db.Column(db.Integer, db.ForeignKey("epics.id"))
    title = db.Column(db.Text, nullable=False)
    role = db.Column(db.Text, nullable=False)
    action = db.Column(db.Text, nullable=False)
    benefit = db.Column(db.Text, nullable=False)
    story_points = db.Column(db.Integer, nullable=True)
    moscow = db.Column(db.String(10), nullable=True)
    rice_reach = db.Column(db.Integer, nullable=True)
    rice_impact = db.Column(db.Float, nullable=True)
    rice_confidence = db.Column(db.Integer, nullable=True)
    rice_effort = db.Column(db.Float, nullable=True)

    project_backlog = db.relationship(
        "ProjectBacklog",
        back_populates="user_stories",
    )
    sprint_backlog = db.relationship("SprintBacklog", back_populates="user_stories")
    epic = db.relationship("Epic", back_populates="user_stories")
    acceptance_criteria = db.relationship(
        "AcceptanceCriteria",
        back_populates="user_story",
        cascade="all, delete-orphan",
    )

    @property
    def rice_score(self):
        """Pontuação RICE, disponível somente quando todos os fatores existem."""
        values = (
            self.rice_reach,
            self.rice_impact,
            self.rice_confidence,
            self.rice_effort,
        )
        if any(value is None for value in values) or self.rice_effort == 0:
            return None
        return round(
            (self.rice_reach * self.rice_impact * (self.rice_confidence / 100))
            / self.rice_effort,
            2,
        )
