from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pale green")
        self.penup()
        self.setpos(0,0)
        self.shapesize(1,1)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.y_move *= -1
    
    def pad_bounce(self):
        self.x_move *= -1

    def resetposition(self):
        self.setpos(0,0)
        self.x_move *= -1
        self.y_move *= -1
        
    
        
