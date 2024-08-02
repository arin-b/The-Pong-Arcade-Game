from turtle import Screen
from net import Net
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()

net = Net()
ball = Ball()

screen.listen()
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
screen.onkey(r_paddle.move_paddle_up, "Up")
screen.onkey(r_paddle.move_paddle_down, "Down")
screen.onkey(l_paddle.move_paddle_up, "w")
screen.onkey(l_paddle.move_paddle_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_off_paddle()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_off_paddle()

    # detect when ball misses right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect when ball misses left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()