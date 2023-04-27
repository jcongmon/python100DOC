from turtle import Turtle

MOVE_DIST = 20


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.turtlesize(stretch_len=5.0, stretch_wid=1.0)
        self.penup()
        self.speed("fastest")
        self.goto(x_cor, y_cor)

    def move_up(self):
        y_cord = self.ycor() + MOVE_DIST
        self.goto(self.xcor(), y_cord)

    def move_down(self):
        y_cord = self.ycor() - MOVE_DIST
        self.goto(self.xcor(), y_cord)

