from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.secret_key = "hello"
Bootstrap(app)


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email(), Length(min=5, max=30)])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=30)])
    submit = SubmitField(label="Log In")

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        valid_email = "admin@email.com"
        valid_password = "12345678"
        if valid_email == form.email.data and valid_password == form.password.data:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)