from flask import Flask, render_template, request
import requests
import smtplib
import os
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

app = Flask(__name__)

response = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
data = response.json()


@app.route("/")
def home():
    return render_template("index.html", data=data)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        message = f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=PASSWORD)
            connection.sendmail(from_addr=USERNAME, to_addrs=USERNAME, msg=f"Subject: New Message\n\n {message}")
        return render_template("contact.html", msg="Successfully received your message.")
    return render_template("contact.html", msg="Contact Me")

@app.route("/<int:id>/")
def post(id):
    for entry in data:
        if entry['id'] == id:
            return render_template("post.html", data=entry)


if __name__ == "__main__":
    app.run(debug=True)
