from turtle import Turtle, Screen
import time #imports the time module

screen = Screen()
screen.setup(width=600, height=600) #screen' width and height set to 600pixels
screen.bgcolor("black") #screen's bgcolor set to black
screen.title("SNAKE GAME") #set title for the screen
screen.tracer(0) #tracer takes a number as input and it turns the animation on/off 0 = off, 1 = on


starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position) #turtle.goto() makes the turtle to go to the x and y coordinate thats specified
    segments.append(new_segment)
screen.update()

game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)
        time.sleep(0.1)  # sleep time is set to 1 second
    screen.update() #whern tracer is off, we use update() to tell program to refresh and redraw the screen












screen.exitonclick()
