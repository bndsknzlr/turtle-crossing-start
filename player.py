from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.setheading(90)
        self.dir_x = 0
        self.goto(STARTING_POSITION)

    def player_move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.dir_x, new_y)

    def reset_player(self):
        pass


# TODO 1. create multiple cars