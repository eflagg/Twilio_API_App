from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Message(db.Model):
    """Course model."""

    __tablename__ = "messages"

    message_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    to = db.Column(db.String, nullable=False)
    body = db.Column(db.Text, nullable=False)
    message_sid = db.Column(db.String)

    def __repr__(self):
        return "<To: %s, Body: %s>" % (self.to, self.body)

class PhoneNumber(db.Model):
    """Phone number model."""

    __tablename__ = "phone_numbers"