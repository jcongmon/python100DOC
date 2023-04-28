from turtle import Screen
from cars import Car
from player import Player
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

cars = []

player = Player()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    if len(cars) < 9 + scoreboard.level:
        for _ in range(random.randint(0, 1)):
            car = Car(scoreboard.level - 1)
            cars.append(car)
    for car in cars:
        car.move()
        if car.xcor() <= -280:
            car.hideturtle()
            car.clear()
            cars.remove(car)
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() >= 255:
        scoreboard.update_score()
        player.go_home()

    screen.onkey(fun=player.move, key="Up")
    screen.listen()

screen.exitonclick()
