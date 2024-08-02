from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.pensize(2)
        self.create_net()

    def create_net(self):
        self.penup()
        self.goto(x=0, y=-300)
        self.left(90)
        for i in range(1, 18):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)