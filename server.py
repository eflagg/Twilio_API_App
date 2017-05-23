from flask import Flask, request, render_template, redirect, flash
import os
from send_sms import send_message

app = Flask(__name__)

app.secret_key = "SECRET"


@app.route('/')
def show_text_form():
    """Show user text form"""

    return render_template("index.html")


@app.route('/send', methods=["POST"])
def send_twilio_message():
    """Send user's message"""

    phone = request.form.get("phone")
    body = request.form.get("message")

    status = send_message(phone, body)

    flash("Message Status: " + status)

    return redirect("/")


if __name__ == "__main__":

    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)