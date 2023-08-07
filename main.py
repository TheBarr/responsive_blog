from flask import Flask, render_template, request
import requests

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
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(name, email, phone, message)
        return "<h1> Successfully sent your message."
    else:
        return render_template("contact.html")


@app.route("/post/<int:id>")
def get_post(id):
    requested_post = None
    for post in posts_data:
        if post["id"] == id:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
