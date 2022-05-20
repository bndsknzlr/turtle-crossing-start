from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.write(f"Level: {self.score}", align="left", font=FONT)

    def add_score(self):
        self.score += 1

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)