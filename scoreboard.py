from turtle import Turtle

class Score(Turtle):
    def __init__(self,position_1,position_2,user_name):
        super().__init__()
        self.score=0
        self.color("white")
        self.shapesize(3,2)
        self.penup()
        self.goto(position_1,position_2)
        self.write(f"{user_name}={self.score} ",align="center",font=("Arial",15,"normal"))
        self.hideturtle()
    
    def increase_score(self,user_name):
        self.score+=1
        self.clear()
        self.write(f"{user_name}={self.score} ",align="center",font=("Arial",15,"normal"))

    


    
