from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.listen()
screen.tracer(0)

score = ScoreBoard()
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

speed = 5

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed("fast")

    # Detect collision with wall if missed
    if ball.xcor() > 380:
        ball.reset()
        score.l_points()

    if ball.xcor() < - 380:
        ball.reset()
        score.r_points()

screen.exitonclick()
