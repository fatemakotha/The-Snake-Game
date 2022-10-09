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
    screen.update() #whern tracer is off, we use update() to tell program to refresh and redraw the screen
    time.sleep(1)  # sleep time is set to 1 second

    #HERE range is 2-0, which means this loop repeats for 2 values: 2, 2-1=1, and not 0. Because range is exclusive of last value
    for seg_num in range(len(segments) - 1, 0, -1): #MOVES 3RD piece to 2DN pieces' location #AND #MOVES 2ND piece to 1ST pieces' location
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(x=new_x, y=new_y) #the last piece moves to the second to last segment's position

    segments[0].forward(20)
    segments[0].left(90)







screen.exitonclick()
