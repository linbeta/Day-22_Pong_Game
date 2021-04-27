from turtle import Turtle
import random
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
        self.auto_ud = 20
        self.auto_speed = AUTO_SPEED

    def move_up(self):
        if self.ycor() > 140:
            pass
        else:
            self.goto(self.xcor(), self.ycor() + 25)

    def move_down(self):
        if self.ycor() < -130:
            pass
        else:
            self.goto(self.xcor(), self.ycor() - 25)

    def auto_up(self):
        if self.ycor() > 140:
            pass
        else:
            new_y = self.ycor() + self.auto_ud * self.auto_speed
            self.goto(self.xcor(), new_y)

    def auto_down(self):
        if self.ycor() < -130:
            pass
        else:
            new_y = self.ycor() - self.auto_ud * self.auto_speed
            self.goto(self.xcor(), new_y)

    def computer(self, ball_position):
        ball_y = ball_position[1]
        if ball_y > self.ycor():
            self.auto_up()
        elif ball_y < self.ycor():
            self.auto_down()

    def reset_position(self):
        self.auto_speed = AUTO_SPEED
        self.goto(self.xcor(), 0)

