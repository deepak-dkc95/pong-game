from turtle import Turtle
MOVE_DIST = 20


class Paddle(Turtle):
    def __init__(self, positions):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(positions)

    def up(self):
        new_y = self.ycor() + MOVE_DIST
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DIST
        self.goto(self.xcor(), new_y)
