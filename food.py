from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #generally the turtle is 20/20, but we want to half it
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)