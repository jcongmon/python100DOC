from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_one = 0
        self.player_two = 0
        self.penup()
        self.color("black")
        self.goto(0, 260)
        self.hideturtle()
        self.update_board()

    def update_score(self, player):
        if player == 1:
            self.player_one += 1
        elif player == 2:
            self.player_two += 1
        self.update_board()

    def update_board(self):
        self.cls()
        self.write(arg=f"{self.player_one}\t{self.player_two}", align="center", font=("Arial", 28, "normal"))

    def cls(self):
        self.clear()
