from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")
MOVE = False


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.tally = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.tally} ", move=MOVE, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=MOVE, align=ALIGNMENT, font=FONT)

    def score(self):
        self.tally += 1
        self.clear()
        self.update_score()



