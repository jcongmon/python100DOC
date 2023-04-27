from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.title("Pong")

player_one = Paddle(-280, 0)
player_two = Paddle(280, 0)
ball = Ball()
score = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce(paddle=False)
    elif (ball.distance(player_one) <= 50 and ball.xcor() < -260) or \
            (ball.distance(player_two) <= 50 and ball.xcor() > 260):
        ball.bounce(paddle=True)
    elif ball.xcor() < -280:
        score.update_score(player=2)
        ball.reset_ball()
    elif ball.xcor() > 280:
        score.update_score(player=1)
        ball.reset_ball()

    screen.onkey(fun=player_one.move_up, key="w")
    screen.onkey(fun=player_one.move_down, key="s")
    screen.onkey(fun=player_two.move_up, key="Up")
    screen.onkey(fun=player_two.move_down, key="Down")
    screen.listen()

screen.exitonclick()
