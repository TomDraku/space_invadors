import turtle


class Ship(turtle.Turtle):
    # konstruowanie statku 
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.shape = "triangle"
        self.setheading(90)
        self.shapesize(stretch_wid=2,stretch_len=2, outline=2)
        self.goto(0, -230)
        self.showturtle()
    
    # funkcja umożliwiająca przesuwanie statku w prawo    
    def move_right(self):
        if self.xcor() < 380:
            self.setx(self.xcor()+30)
    
    # funkcja umożliwiająca przesuwanie statku w lewo    
    def move_left(self):
        if self.xcor() > -380:
            self.setx(self.xcor()-30)
        
    
        