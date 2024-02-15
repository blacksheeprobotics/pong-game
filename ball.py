from turtle import Turtle

UPPER_BOUND = 290
LOWER_BOUND = -290
OFFSET_X = 10
OFFSET_Y = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.width = 20
        self.height = 20

    def move(self):
        global OFFSET_X, OFFSET_Y

        new_x = self.xcor() + OFFSET_X
        new_y = self.ycor() + OFFSET_Y

        if new_y >= UPPER_BOUND:
            new_y = UPPER_BOUND
            OFFSET_Y = -OFFSET_Y

        if new_y <= LOWER_BOUND:
            new_y = LOWER_BOUND
            OFFSET_Y = -OFFSET_Y

        self.goto(new_x, new_y)
