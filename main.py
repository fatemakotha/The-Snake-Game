from turtle import Turtle, Screen

#Setting up the screen:
screen = Screen()
screen.setup(width=600, height=600) #sets the screen dimension
screen.bgcolor("black")
screen.title("Snake Game")

x_positions = [0, -20, -40]
all_turtles = []

for turtle_index in range(0, 3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.goto(x=x_positions[turtle_index], y=0)



























screen.exitonclick()