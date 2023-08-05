import turtle


class Alien(turtle.Turtle):
    # konstruowanie statku obcych
    def __init__(self, color, position):
        super().__init__()
        self.direction = 1
        self.speed = 10
        self.hideturtle()
        self.penup()
        self.color(color)
        self.shape = "triangle"
        self.setheading(270)
        self.shapesize(stretch_wid=2,stretch_len=2, outline=2)
        self.goto(position)
        self.showturtle()
        
        
    # funkcja umożliwiająca przesuwanie statku   
    def move(self):
        if self.xcor() < 380:
            self.setx(self.xcor() + self.speed * self.direction)
            if self.xcor() >= 360:
                self.sety(self.ycor()-100)
                self.direction = -1
            elif self.xcor() <= -360:
                self.sety(self.ycor()-100)
                self.direction = 1
        
                
    
    