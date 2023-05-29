from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
data = response.json()

@app.route("/")
def home():
    return render_template("index.html", data=data)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/<int:id>/")
def post(id):
    for entry in data:
        if entry['id'] == id:
            return render_template("post.html", data=entry)


if __name__ == "__main__":
    app.run(debug=True)
