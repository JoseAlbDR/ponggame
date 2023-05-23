from turtle import *


class Paddle(Turtle):
    def __init__(self, player_number):
        super().__init__()
        self.player_number = player_number
        self.x = 0
        self.y = 0
        self.set_player()
        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=self.x, y=self.y)

    def set_player(self):
        if self.player_number == 1:
            self.x = 350
            self.y = 0
        else:
            self.x = -360
            self.y = 0

    def up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(x=self.x, y=new_y)

    def down(self):
        if self.ycor() > -220:
            new_y = self.ycor() - 20
            self.goto(x=self.x, y=new_y)
