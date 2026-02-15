from turtle import Turtle





class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("day20-21-Snake-Game/score.txt") as data:
                content = data.read().strip()
                self.high_score = int(content) if content else 0
        except (FileNotFoundError, ValueError):
            self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=260)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))


    def add_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()
        self.score = 0
        self.update_scoreboard()

    def _save_high_score(self):
        with open("day20-21-Snake-Game/score.txt", "w") as data:
            data.write(str(self.high_score))


