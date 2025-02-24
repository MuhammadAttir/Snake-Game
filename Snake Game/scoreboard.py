from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.speed(0)
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_score()
        
    def Game_Over(self):
        self.goto(0,0)
        self.write("Game Over!",align="center",font=("Arial",24,"normal"))
        
    def increase_score(self):
        self.clear()
        self.score+=5
        self.update_score()
        
    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        