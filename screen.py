from turtle import Turtle

class MyScreen(Turtle):
    def __init__(self):
        super().__init__()
        self.net = Turtle()
        self.create()

    def create(self):
        self.bgcolor("black")
        self.title("Pong Game")
        self.tracer(0)
        self.setup(width=800, height=600, startx=0, starty=0)

    def net(self):
        self.net = Turtle()
        self.net.penup()
        self.net.color("white")
        self.net.speed(0)
        self.net.goto(x=0, y=300)
        self.net.setheading(270)
        for n in range(26):
            self.net.pendown()
            self.net.forward(20)
            self.net.penup()
            self.net.forward(20)