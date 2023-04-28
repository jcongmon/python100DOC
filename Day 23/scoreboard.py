from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.goto(-200, 280)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level {self.level}:", align="left", font=("Arial", 16, "normal"))

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align="center", font=("Arial", 24, "normal"))
