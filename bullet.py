import turtle


class Bullet(turtle.Turtle):
    # konstruowanie pocisku 
    def __init__(self, ship, heading):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
        self.shape("triangle")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5, outline=0.5)
        self.setheading(heading)
        self.goto((ship.xcor()), (ship.ycor()))
        self.showturtle()
        self.speed = 2
        
    def move(self):
        self.forward(self.speed)