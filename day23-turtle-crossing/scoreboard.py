from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.goto(-250, 250)
        self.write(f"Level: {self.score}", align="center", font=("Arial", 24, "normal"))

    def level_up(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Arial", 24, "normal"))

