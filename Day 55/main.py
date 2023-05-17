from flask import Flask
import random

random_num = random.randint(0, 9)
app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=400>"


@app.route("/<int:num>")
def check_value(num):
    if num > random_num:
        return "<h1 style='color:red'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=400>"
    elif num < random_num:
        return "<h1 style='color:brown'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width=400>"
    else:
        return "<h1 style='color:green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width=400>"


if __name__ == "__main__":
    app.run(debug=True)
