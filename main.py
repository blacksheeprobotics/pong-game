import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

ball = Ball()

right_paddle = Paddle((360, 0))
left_paddle = Paddle((-360, 0))
screen.update()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "a")
screen.onkey(left_paddle.down, "z")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    # detect collision with left paddle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect ball going past right paddle - score!
    if ball.xcor() > 380:
        ball.reset_position()

    # detect ball going past left paddle - score!
    if ball.xcor() < -380:
        ball.reset_position()

    ball.move()

screen.exitonclick()
