from turtle import Turtle

class Player(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("White")
        self.shapesize(5,1)
        self.goto(position)
        self.penup()

    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)
    
    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)