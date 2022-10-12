from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
#................

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] #only works after snake is created


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)  # turtle.goto() makes the turtle to go to the x and y coordinate thats specified
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position()) #takes the last segment which is at index -1


    def move(self):
        # HERE range is 2-0, which means this loop repeats for 2 values: 2, 2-1=1, and not 0. Because range is exclusive of last value
        for seg_num in range(len(self.segments) - 1, 0, -1):  # MOVES 3RD piece to 2DN pieces' location #AND #MOVES 2ND piece to 1ST pieces' location
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)  # the last piece moves to the second to last segment's position
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN: #Checks the current heading and if it going down, it can't go up
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:  # Checks the current heading and if it going UP, it can't go down
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)