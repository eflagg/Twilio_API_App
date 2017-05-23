from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Message(db.Model):
    """Course model"""

    __tablename__ = "messages"

    message_id = db.Column(db.String, primary_key=True, nullable=False)
    to = db.Column(db.String, nullable=False)
    body = db.Column(db.Text, nullable=False)


    def __repr__(self):
        """Create repr for easier reading when debugging"""

        return "<To: %s, Body: %s>" % (self.to, self.body)


def connect_to_db(app, db_uri='postgresql:///twilio_app'):
    """Connect the database to Flask app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)
    db.create_all()


if __name__ == "__main__":

    from server import app

    connect_to_db(app)
