from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.level = 1
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increasing_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.write(f"Level: {self.level}", align="center", font=FONT)
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)


