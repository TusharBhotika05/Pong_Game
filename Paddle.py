from turtle import Turtle


class paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("light sky blue")
        self.penup()
        self.shape("square")
        self.setpos(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
        
    def move_up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)   
    
    def move_down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)


    
          


    
    

    