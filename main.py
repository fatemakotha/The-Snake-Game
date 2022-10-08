from turtle import Turtle, Screen

#Setting up the screen:
screen = Screen()
screen.setup(width=600, height=600) #sets the screen dimension
screen.bgcolor("black")
screen.title("Snake Game")

x_positions = [0, -20, -40]
all_turtles = []


segment_1 = Turtle(shape="square")
segment_1.color("white")
segment_1.goto(x=0, y=0)

segment_2 = Turtle(shape="square")
segment_2.color("white")
segment_2.goto(x=-20, y=0)

segment_3 = Turtle(shape="square")
segment_3.color("white")
segment_3.goto(x=-40, y=0)


























screen.exitonclick()