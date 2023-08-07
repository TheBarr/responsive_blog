from flask import Flask, render_template
import requests

posts_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
app = Flask(__name__)


@app.route("/")
def get_home():
    return render_template("index.html", posts_data=posts_data)


@app.route("/about")
def get_about():
    return render_template("about.html")


@app.route("/contact")
def get_contact():
    return render_template("contact.html")

@app.route("/post/<int:id>")
def get_post(id):
    for post in posts_data:
        if post["id"] == id:
            desired_post = post
    return render_template("post.html", post=desired_post)



if __name__ == "__main__":
    app.run(debug=True)
