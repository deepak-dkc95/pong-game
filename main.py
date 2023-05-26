from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("THE PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

r_scoreboard = ScoreBoard((200, 240))
l_scoreboard = ScoreBoard((-200, 240))

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 70 and ball.xcor() > 310) or (ball.distance(l_paddle) < 70 and ball.xcor() < -310):
        ball.bounce_x()

    if ball.xcor() > 380:
        l_scoreboard.update_score()
        ball.reset_position()
    elif ball.xcor() < -380:
        r_scoreboard.update_score()
        ball.reset_position()

screen.exitonclick()
