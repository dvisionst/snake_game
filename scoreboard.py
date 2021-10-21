from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "bold")
MOVE = False


class Scoreboard(Turtle):

    def __init__(self, name):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.tally = 0
        self.current_user = name
        with open("data.txt") as file:
            contents = file.read()
        self.high_score = int(contents[0])
        self.user_high = contents[2:]
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.current_user} your score: {self.tally} "
                   f"High: {self.high_score} by {self.user_high}",
                   move=MOVE, align=ALIGNMENT, font=FONT)

    def reset_s(self):
        if self.tally > self.high_score:
            self.high_score = self.tally
            self.user_high = self.current_user
            with open("data.txt", mode="w") as nfile:
                nfile.write(f"{self.high_score} {self.user_high}")
        self.tally = 0
        self.update_score()

    def score(self):
        self.tally += 1
        self.update_score()


