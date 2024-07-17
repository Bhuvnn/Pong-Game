from turtle import Turtle,Screen
from Control import Player
from ball import Ball
from scoreboard import Score
import time
screen=Screen()
screen.setup(800,600)
user_1=screen.textinput("Entry","Enter Your name, Player 1")
user_2=screen.textinput("Entry","Enter Your name, Player 2")
screen.title("Pong")
screen.bgcolor("Black")
screen.tracer(0)
#Creation of centre line

turtle=Turtle()
screen.listen()
turtle.setposition(0,-290)
turtle.color("White")
turtle.width(3)
turtle.setheading(90)
turtle.speed(0)

#creation of the player
player_2=Player((350,0))
screen.onkey(player_2.go_up,"Up")
screen.onkey(player_2.go_down,"Down")

player_1=Player((-350,0))
screen.onkey(player_1.go_up,"w")
screen.onkey(player_1.go_down,"s")



for i in range(0,600):
    turtle.forward(50)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()

#adding a ball
ball=Ball() 
score_1=Score(-160,280,user_1)
score_2=Score(160,280,user_2)


game=True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #Detect collison from the wall
    if ball.ycor()>290 or ball.ycor()<-290:
       ball.bounce_y()

    if ball.distance(player_2)<60 and ball.xcor()>320 or ball.distance(player_1)<60 and ball.xcor()<-320:
        ball.bounce_x()
        
   
    if ball.distance(player_2)>60 and ball.xcor()>400:  
        ball.reset_position()
        player_2.goto(350,0)
        player_1.goto(-350,0)
        score_1.increase_score(user_1)
    
    elif ball.distance(player_1)>60 and ball.xcor()<-400:
        ball.reset_position()
        player_1.goto(-350,0)
        player_2.goto(350,0)
        score_2.increase_score(user_2)
    

    

    
screen.exitonclick()
