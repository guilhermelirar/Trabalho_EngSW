from app.models import db


class AcceptanceCriteria(db.Model):
    __tablename__ = "acceptance_criteria"

    id = db.Column(db.Integer, primary_key=True)
    user_story_id = db.Column(
        db.Integer,
        db.ForeignKey("user_stories.id"),
        nullable=False,
    )
    title = db.Column(db.Text, nullable=False)
    given = db.Column(db.Text, nullable=False)
    when = db.Column(db.Text, nullable=False)
    then = db.Column(db.Text, nullable=False)

    user_story = db.relationship("UserStory", back_populates="acceptance_criteria")
