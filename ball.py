from turtle import Turtle
import time
BALL_SPEED = 0.02


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 4.5
        self.ball_speed = BALL_SPEED

    def move(self):
        # Could set the factor inside forward to make the ball move slower
        new_x = self.xcor() + self.x_move * self.ball_speed
        new_y = self.ycor() + self.y_move * self.ball_speed
        self.goto(new_x, new_y)

    def collision_paddle(self):
        self.x_move *= -1
        self.ball_speed += 0.001
        self.move()

    def wall_bounce(self):
        self.y_move *= -1
        self.move()

    def reset_position(self):
        self.ball_speed = BALL_SPEED
        self.goto(0, 0)
        self.x_move *= -1
        time.sleep(1)
