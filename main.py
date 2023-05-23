import time
from paddle import *
from ball import Ball
from scoreboard import Score
from random import choice


def listeners(player):
    screen.listen()
    if player.player_number == 1:
        screen.onkeypress(player.up, "Up")
        screen.onkeypress(player.down, "Down")
    else:
        screen.onkeypress(player.up, "w")
        screen.onkeypress(player.down, "s")


def net():
    my_net = Turtle()
    my_net.penup()
    my_net.color("white")
    my_net.speed(0)
    my_net.goto(x=0, y=300)
    my_net.setheading(270)
    for n in range(26):
        my_net.pendown()
        my_net.forward(20)
        my_net.penup()
        my_net.forward(20)


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
screen.setup(width=800, height=600, startx=0, starty=0)

net()
player1 = Paddle(1)
player2 = Paddle(2)
ball = Ball(choice([1, 2]))
score1 = Score(1)
score2 = Score(2)

listeners(player1)
listeners(player2)

game_is_on = True
while game_is_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()

    if ball.ycor() == 280:
        if ball.direction == "right_up":
            ball.bounce("right_down")
        elif ball.direction == "left_up":
            ball.bounce("left_down")

    if ball.ycor() == -280:
        if ball.direction == "left_down":
            ball.bounce("left_up")
        elif ball.direction == "right_down":
            ball.bounce("right_up")

    if ball.distance(player1) < 40:
        ball.set_speed(0.9)
        if ball.direction == "right_up":
            ball.bounce("left_up")
        elif ball.direction == "right_down":
            ball.bounce("left_down")

    if ball.distance(player2) < 40:
        ball.set_speed(0.9)
        if ball.direction == "left_up":
            ball.bounce("right_up")
        elif ball.direction == "left_down":
            ball.bounce("right_down")

    if ball.xcor() > 400:
        score2.add_score()
        ball = Ball(2)
    elif ball.xcor() < -400:
        score1.add_score()
        ball = Ball(1)

screen.exitonclick()
