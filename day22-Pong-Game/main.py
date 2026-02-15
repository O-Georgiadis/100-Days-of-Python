from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)



l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")



game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision
    if  ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()



    # Detect missed Collision
    if ball.xcor() > 380:
        ball.reset()
        ball.paddle_bounce()
        ball.bounce()
        score.l_point()
 
    
    if ball.xcor() < -380:
        ball.reset()
        ball.paddle_bounce()
        ball.bounce()
        score.r_point()
       

screen.exitonclick()