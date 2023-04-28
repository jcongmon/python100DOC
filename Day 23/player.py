from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.go_home()

    def move(self):
        self.forward(10)

    def go_home(self):
        self.goto(0, -270)
