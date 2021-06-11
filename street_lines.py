
from turtle import Turtle

FINISH_LINE_Y = 280

class Street_lines(Turtle):
    def __init__(self):
        super().__init__()
        """Finish Line"""
        self.hideturtle()
        self.pencolor("white")
        for y_coord in range(-240,280,40):
            self.draw_line(y_coordinate = y_coord)
    
    def draw_line(self, y_coordinate):
        self.penup()
        self.goto(-300,y_coordinate)
        self.setheading(0)
        """Dashed Line"""
        for i in range(150):
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(5)


