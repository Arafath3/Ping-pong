from turtle import Turtle

POSITION = [(380, 0), (-380, 0)]


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles = []
        self.create_paddle()

    def create_paddle(self):
        for paddle in POSITION:
            new_paddle = Turtle("square")
            new_paddle.shapesize(stretch_wid=4, stretch_len=.7)
            new_paddle.penup()
            new_paddle.color("white")
            new_paddle.goto(paddle)
            self.paddles.append(new_paddle)
