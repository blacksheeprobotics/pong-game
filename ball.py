from turtle import Turtle

UPPER_BOUND = 290
LOWER_BOUND = -290


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.width = 20
        self.height = 20
        self.x_move = 10
        self.y_move = 10

    def move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
