from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"SCORE: {self.score}", align="center", font=("Arial", 24, "normal")) #the write() function takes in an input and alignment and a font



