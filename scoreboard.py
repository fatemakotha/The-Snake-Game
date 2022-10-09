from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle() #the turtle dissapears
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)  # the write() function takes in an input and alignment and a font


    def game_over(self):
        self.goto(x=0, y=0)

        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

