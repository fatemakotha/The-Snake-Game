from turtle import Turtle, Screen
import time

# Setting up the screen:
screen = Screen()
screen.setup(width=600, height=600)  # sets the screen dimension
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # tracer set to 0

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

# Creating the snake body
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)
        screen.update()  # screen updated after 3 objects have been created
        time.sleep(1)  # adds 1 sec delay after each segment moves










screen.exitonclick()
