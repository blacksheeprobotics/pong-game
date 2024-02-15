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

    ball.move()

screen.exitonclick()
