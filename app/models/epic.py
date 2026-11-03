from app.models import db


class Epic(db.Model):
    __tablename__ = "epics"

    id = db.Column(db.Integer, primary_key=True)
    project_backlog_id = db.Column(
        db.Integer,
        db.ForeignKey("project_backlogs.id"),
        nullable=False,
    )
    title = db.Column(db.Text, nullable=False)

    project_backlog = db.relationship("ProjectBacklog", back_populates="epics")
    user_stories = db.relationship("UserStory", back_populates="epic")
