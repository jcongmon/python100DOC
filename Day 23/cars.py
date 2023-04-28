from turtle import Turtle
import random

COLORS = ["red", "orange", "green", "blue", "purple"]
X_DIST = 280


class Car(Turtle):
    def __init__(self, inc_speed):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color_choice = random.randint(0, 4)
        self.y_init = random.randint(-200, 250)
        self.goto(X_DIST, self.y_init)
        self.shapesize(stretch_wid=1.0, stretch_len=2.0)
        self.color(COLORS[self.color_choice])
        self.move_speed = -random.randint(2, 10) - inc_speed

    def move(self):
        new_x = self.xcor() + self.move_speed
        self.goto(new_x, self.y_init)
