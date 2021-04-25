from turtle import Turtle
FONT = ("Courier New", 30, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.ht()
        self.goto(0, 150)
        self.write(f"{self.left_score} : {self.right_score}", align="center", font=FONT)

    def refresh(self):
        self.clear()
        self.write(f"{self.left_score} : {self.right_score}", align="center", font=FONT)
