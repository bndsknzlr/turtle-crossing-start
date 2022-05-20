from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.y_pos = random.randrange(-220, 220, 5)
        self.x_pos = 100
        self.x_distance = STARTING_MOVE_DISTANCE
        self.goto(self.x_pos, self.y_pos)
        self.cruising = True

    def move_cars(self):
        self.forward(self.x_distance)

    def speed_up_level(self):
        self.x_distance += MOVE_INCREMENT



# TODO 1. create multiple cars

# TODO 3. speed up cars after level up
# TODO 4. pick random y - axis position

