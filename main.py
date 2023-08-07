from flask import Flask, render_template, request
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

posts_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
app = Flask(__name__)


@app.route("/")
def get_home():
    return render_template("index.html", posts_data=posts_data)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def get_contact():
    if request.method == 'POST':
        with smtplib.SMTP("smtp.gmail.com") as conn:
            conn.starttls()
            conn.login(user=os.getenv("FROM_EMAIL"), password=os.getenv("PASSWORD"))
            conn.sendmail(
                from_addr=os.getenv("from_email"),
                to_addrs=os.getenv("TO_EMAIL"),
                msg=f"Subject: New Message\n\n Name: {request.form['name']}\n Email: {request.form['email']}\n "
                    f"Phone: {request.form['phone']}\n Message: {request.form['message']}"
            )
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:id>")
def get_post(id):
    requested_post = None
    for post in posts_data:
        if post["id"] == id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
