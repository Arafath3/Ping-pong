from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, tup):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=.7)
        self.penup()
        self.color("white")
        self.goto(tup)

    def up(self):
        y_new = self.ycor() + 20
        self.goto(self.xcor(), y_new)

    def down(self):
        y_new = self.ycor() - 20
        self.goto(self.xcor(), y_new)



