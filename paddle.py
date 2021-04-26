from turtle import Turtle
AUTO_SPEED = 0.01


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.speed("fastest")
        self.goto(position)
        self.auto_ud = 30
        self.auto_speed = AUTO_SPEED

    def move_up(self):
        if self.ycor() > 140:
            pass
        else:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() < -130:
            pass
        else:
            self.goto(self.xcor(), self.ycor() - 20)

    def auto_up_down(self):
        new_y = self.ycor() + self.auto_ud * self.auto_speed
        self.goto(self.xcor(), new_y)

    def computer(self):
        self.auto_up_down()
        if self.ycor() > 150:
            self.auto_ud *= -1
        elif self.ycor() < -150:
            self.auto_ud *= -1

    def reset_position(self):
        self.auto_speed = AUTO_SPEED
        self.goto(self.xcor(), 0)

