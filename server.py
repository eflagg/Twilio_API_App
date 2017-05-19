from flask import Flask, request, render_template
import os

app = Flask(__name__)

app.secret_key = "SECRET"


@app.route('/')
def show_text_form():
    """Show user text form"""

    return render_template("index.html")


@app.route('/send', methods=["POST"])
def send_message():
    """Send user's message"""

    phone = request.form.get("phone")
    message = request.form.get("message")

    from twilio.rest import Client

    # put your own credentials here
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token = "your_auth_token"

    client = Client(account_sid, auth_token)

    client.messages.create(
        to=phone,
        from_="+12027513223",
        body=message)


    return render_template("index.html")


if __name__ == "__main__":

    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)