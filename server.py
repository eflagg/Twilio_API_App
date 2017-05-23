from flask import Flask, request, render_template, redirect, flash
import os
from helpers import send_message, add_msg_to_db
from model import connect_to_db

app = Flask(__name__)

app.secret_key = "SECRET"


@app.route('/')
def show_text_form():
    """Show user text form"""

    return render_template("index.html")


@app.route('/send', methods=["POST"])
def send_twilio_message():
    """Send user's message, return homepage with success message"""

    phone = request.form.get("phone")
    body = request.form.get("body")

    message = send_message(phone, body)

    add_msg_to_db(message.sid, phone, body)

    flash("You have successfully sent your message!")

    return redirect("/")


if __name__ == "__main__":

    connect_to_db(app)
    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)