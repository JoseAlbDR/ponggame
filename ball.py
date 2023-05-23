from turtle import Turtle
from random import choice

EAST_X = 390
NORTH_Y = 290


class Ball(Turtle):
    def __init__(self, player):
        super().__init__()
        self.movement_x = 0
        self.movement_y = 0
        self.direction = ""
        self.player = player
        self.shape("circle")
        self.color("white")
        self.penup()
        self.movements = {"right_down": [10, -10], "right_up": [10, 10], "left_down": [-10, -10], "left_up": [-10, 10]}
        self.player_ball()
        self.movement_speed = 0.1

    def move(self, ):
        for directions in self.movements:
            if directions == self.direction:
                new_x = self.xcor() + self.movements[self.direction][0]
                new_y = self.ycor() + self.movements[self.direction][1]
                self.direction = self.direction
                self.goto(x=new_x, y=new_y)

    def bounce(self, direction):
        for directions in self.movements:
            if directions == direction:
                self.movement_x = self.movements[direction][0]
                self.movement_y = self.movements[direction][1]
                self.direction = direction

    def player_ball(self):
        if self.player == 1:
            directions = ["left_up", "left_down"]
            self.direction = choice(directions)
            self.move()
        elif self.player == 2:
            directions = ["right_up", "right_down"]
            self.direction = choice(directions)
            self.move()

    def set_speed(self, multiplier):
        self.movement_speed *= multiplier
