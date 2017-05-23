def send_message(phone, body):

    from twilio.rest import Client
    import os

    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=phone,
        from_=os.environ['TWILIO_PHONE_NUMBER'],
        body=body)

    return message.status