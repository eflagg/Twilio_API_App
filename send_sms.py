def send_message(phone, message):

    from twilio.rest import Client

        account_sid = TWILIO_ACCOUNT_SID
        auth_token = TWILIO_AUTH_TOKEN

        client = Client(account_sid, auth_token)

        client.messages.create(
            to=phone,
            from_=TWILIO_PHONE_NUMBER,
            body=message)