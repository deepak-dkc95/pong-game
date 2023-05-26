from turtle import Turtle
FONT = ("Courier", 40, "bold")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.color("white")
        self.write_score()

    def write_score(self):
        self.write(arg=self.score, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()
