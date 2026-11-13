# Modelo para uma história de usuário
from app.models import db


class UserStory(db.Model):
    __tablename__ = "user_stories"
    __table_args__ = (
        db.CheckConstraint(
            "story_points IS NULL OR story_points IN (0, 1, 2, 3, 5, 8, 13, 21, 34, 55)",
            name="ck_user_stories_story_points",
        ),
        db.CheckConstraint(
            "moscow IS NULL OR moscow IN ('M', 'S', 'C', 'W')",
            name="ck_user_stories_moscow",
        ),
        db.CheckConstraint(
            "rice_impact IS NULL OR rice_impact IN (0.25, 0.5, 1, 2, 3)",
            name="ck_user_stories_rice_impact",
        ),
        db.CheckConstraint(
            "rice_confidence IS NULL OR rice_confidence IN (50, 80, 100)",
            name="ck_user_stories_rice_confidence",
        ),
    )

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
    moscow = db.Column(db.Text, nullable=True)
    rice_reach = db.Column(db.Integer, nullable=True)
    rice_impact = db.Column(db.Float, nullable=True)
    rice_confidence = db.Column(db.Integer, nullable=True)

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
        effort = self.story_points
        values = (
            self.rice_reach,
            self.rice_impact,
            self.rice_confidence,
            effort,
        )
        if any(value is None for value in values) or effort == 0:
            return None
        return round(
            (self.rice_reach * self.rice_impact * (self.rice_confidence / 100))
            / effort,
            2,
        )

    @property
    def rice_effort(self):
        """Esforço RICE derivado dos Story Points, sem duplicação no banco."""
        return self.story_points
