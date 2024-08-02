from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=0.5)
        self.color("white")
        self.penup()
        self.goto(position)

    def move_paddle_up(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x=x, y=y+20)

    def move_paddle_down(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x=x, y=y-20)