
#importing the necessary modules
from turtle import Turtle, Screen
from Paddle import paddle
from ball import Ball
import time
import scoreboard


#setting up the screen
screen = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor("black")
screen.title("Pong Game")
score = scoreboard.ScoreBoard()

#divider line
line = Turtle()
line.hideturtle()

line.left(90)
line.penup()
line.color("white")
line.setpos(-5,-300)
line.pendown()
for i in range(10):
    
    line.forward(30)
    line.penup()
    line.forward(30)
    line.pendown()

screen.tracer(0)

#paddle
paddle_r = paddle((350, 0))  
paddle_l = paddle((-350, 0))


screen.listen()
#paddle movement
screen.onkeypress(paddle_l.move_up, "w")
screen.onkeypress(paddle_l.move_down, "s")

screen.onkeypress(paddle_r.move_up, "Up")
screen.onkeypress(paddle_r.move_down, "Down")

#game-play
game_is_on = True
ball = Ball()
t = 0.1
while game_is_on:
    
    time.sleep(t)
    screen.update()
    
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.xcor() > 330 or ball.xcor() < -330:
        if ball.distance(paddle_r) < 50 or ball.distance(paddle_l) < 50:
            ball.pad_bounce()
            if t < 0.01:
                pass
            else:
                t -= 0.01
            
            

    if ball.xcor() > 370:
        ball.resetposition()
        score.l_score_up()
        t = 0.1
        
    if ball.xcor() < -370:
        ball.resetposition()
        score.r_score_up()
        t = 0.1

    
        
        


screen.exitonclick()



