from turtle import Turtle


class Score(Turtle):
    def __init__(self, player):
        self.score = 0
        self.player = player
        super().__init__()
        # self.goto(-250, 280)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.player_score()
        self.add_score()

    def add_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("Verdana", 15, "normal"))
        self.score += 1

    def game_over(self):
        self.home()
        self.write("GAME OVER", False, "center", ("Verdana", 15, "bold"))

    def player_score(self):
        if self.player == 1:
            self.goto(150, 270)
        else:
            self.goto(-250, 270)
