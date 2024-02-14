import time
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle1 = Paddle()
paddle1.goto(360,0)
paddle2 = Paddle()
paddle2.goto(-360, 0)
screen.update()

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "a")
screen.onkey(paddle2.down, "z")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()