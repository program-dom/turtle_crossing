from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.pu()
        self.hideturtle()
        self.level = 0
        self.goto(-200, 250)
        self.scoreboard()

    def scoreboard(self):
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
