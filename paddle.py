from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")
        self.goto(position)

    def move_up(self):
        if self.ycor() > 150:
            pass
        else:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() < -130:
            pass
        else:
            self.goto(self.xcor(), self.ycor() - 20)
