from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_coord = -120

for color in colors:
    t = Turtle(shape="turtle")
    t.color(color)
    t.penup()
    t.goto(x=-230, y=y_coord)
    y_coord += 50
    turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        dist = random.randint(0, 10)
        turtle.forward(dist)
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.color()[0]

if user_bet == winner:
    print("You won!")
else:
    print(f"Sorry, you lost. The winner is {winner}.")

screen.exitonclick()
