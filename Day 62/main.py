from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

import pandas as pd

app = Flask(__name__)
app.secret_key = "hello"
Bootstrap(app)


class Cafe(FlaskForm):
    name = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe location on Google Maps(URL)', validators=[DataRequired(), URL(require_tld=False)])
    open = StringField(label='Opening time e.g. 8AM', validators=[DataRequired()])
    close = StringField(label='Closing time e.g. 5:30PM', validators=[DataRequired()])
    coffee = SelectField(label='Coffee Rating', choices=['☕', '☕☕', '☕☕☕', '☕☕☕☕', '☕☕☕☕☕'])
    wifi = SelectField(label='Wifi Rating', choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'])
    socket = SelectField(label='Power Socket Availability', choices=['✘', '🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌',  '🔌🔌🔌🔌🔌'])
    submit = SubmitField(label='Submit')


df = pd.read_csv('cafe-data.csv')


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cafes")
def cafes():
    return render_template("cafes.html", cafes=df)


@app.route("/add", methods=['GET', 'POST'])
def add():
    new_cafe = Cafe()
    if new_cafe.validate_on_submit():
        new_row = [new_cafe.name.data, new_cafe.location.data, new_cafe.open.data, new_cafe.close.data,
                   new_cafe.coffee.data, new_cafe.wifi.data, new_cafe.socket.data]
        df.loc[len(df)] = new_row
        return render_template("cafes.html", cafes=df)
    return render_template("add.html", cafe=new_cafe)


if __name__ == "__main__":
    app.run(debug=True)