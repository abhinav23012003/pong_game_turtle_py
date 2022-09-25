from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

ball = Ball()
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-390, 0))
score = Scoreboard()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "q")
screen.onkey(l_paddle.go_down, "z")


is_game_on = True
while is_game_on:
    time.sleep(score.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()
    if ball.distance(r_paddle) < 40 and ball.xcor() > 350 or ball.distance(l_paddle) < 40 and ball.xcor() < -360:
        ball.bounce_x()
        score.move_speed *= 0.85

    if ball.xcor() > 390:
        ball.restart()
        ball.bounce_x()
        score.l_point()

    if ball.xcor() < -400:
        ball.restart()
        ball.bounce_x()
        score.r_point()

screen.exitonclick()
