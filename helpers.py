from model import db, Message
from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

def add_msg_to_db(mid, to, body):
    """Add message object to db"""

    message = Message(message_id=mid, to=to, body=body)
    db.session.add(message)
    db.session.commit()


def send_message(phone, body):
    """Use Twlio's API library to send message"""

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=phone,
        from_=os.environ['TWILIO_PHONE_NUMBER'],
        body=body)

    return message


