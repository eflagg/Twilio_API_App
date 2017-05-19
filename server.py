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

    print phone, message


    return render_template("index.html")


if __name__ == "__main__":

    PORT = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=PORT)