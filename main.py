from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=400)
screen.bgcolor("#343a40")
screen.title("Pong")
screen.listen()
screen.tracer(0)

# Create a 2 paddles for 2 human users
right_paddle = Paddle((360, 0))
left_paddle = Paddle((-370, 0))

# Use Up and Down keys to move the right_paddle
screen.onkeypress(key="Up", fun=right_paddle.move_up)
screen.onkeypress(key="Down", fun=right_paddle.move_down)

# Use W and S keys to move the left_paddle
screen.onkeypress(key="w", fun=left_paddle.move_up)
screen.onkeypress(key="s", fun=left_paddle.move_down)

# A ball pop-up at the center and move toward the upper-right corner.
ball = Ball()
ball_speed = 0.02
score_board = ScoreBoard()


game_is_on = True
while game_is_on:
    # time.sleep(0.1)
    screen.update()
    # time.sleep(0.05)
    ball.move()
    if ball.ycor() > 190 or ball.ycor() < -180:
        ball.wall_bounce()
    elif ball.distance(right_paddle.pos()) < 50 and ball.xcor() > 340:
        ball.collision_paddle()
    elif ball.distance(left_paddle.pos()) < 50 and ball.xcor() < -355:
        ball.collision_paddle()
    elif ball.xcor() > 400:
        # Left wins, score +1
        score_board.left_score += 1
        score_board.refresh()
        ball.reset_position()
    elif ball.xcor() < -405:
        # Right wins, score +1
        score_board.right_score += 1
        score_board.refresh()
        ball.reset_position()


# Draw a center line

screen.exitonclick()