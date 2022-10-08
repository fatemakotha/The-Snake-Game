from turtle import Turtle, Screen
import time

# Setting up the screen:
screen = Screen()
screen.setup(width=600, height=600)  # sets the screen dimension
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # tracer set to 0







game_is_on = True
while game_is_on:
    screen.update()  # screen updated after 3 objects have been created
    time.sleep(0.1)  # adds 0.1 sec delay after all 3 segments have moved

    for seg_num in range(len(segments) - 1 , 0 , -1): #starts seg_num with value 2 and ends at 0 with -1 as steps
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y) #gets hold of segment[2] which is the last segment and makes it goto the position of second to last segment AND doing this for all segments
    segments[0].forward(20)









screen.exitonclick()
