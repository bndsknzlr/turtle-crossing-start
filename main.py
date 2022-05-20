import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()

screen.listen()

screen.onkey(fun=player.player_move, key="Up")
# score.game_over()
game_is_on = True

cars = CarManager()
while game_is_on:
    cars.move_cars()
    for i in range(7):
        if i == 6:
            cars = CarManager()
            cars.move_cars()
            time.sleep(0.1)
        else:
            cars.move_cars()
            time.sleep(0.1)
    screen.update()


screen.exitonclick()


# TODO 1. create multiple cars
