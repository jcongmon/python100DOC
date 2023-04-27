from turtle import Turtle

MOVE_DIST = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.penup()
        self.speed(0)
        self.x_move = MOVE_DIST
        self.y_move = MOVE_DIST

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce(self, paddle):
        if paddle:
            self.increase_speed()
            self.x_move *= -1
        else:
            self.y_move *= -1

    def increase_speed(self):
        if self.x_move < 0:
            self.x_move -= 2
        elif self.x_move > 0:
            self.x_move += 2

    def reset_ball(self):
        self.home()
        self.x_move = MOVE_DIST
        self.y_move = MOVE_DIST

