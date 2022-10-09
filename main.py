from turtle import Turtle, Screen
import time #imports the time module
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600) #screen' width and height set to 600pixels
screen.bgcolor("black") #screen's bgcolor set to black
screen.title("SNAKE GAME") #set title for the screen
screen.tracer(0) #tracer takes a number as input and it turns the animation on/off 0 = off, 1 = on


snake = Snake()

screen.listen() #starts listening

screen.onkey(key="Up", fun=snake.up) #calls the snake.up function when upward arrow is hit **
screen.onkey(key="Down", fun=snake.down) #calls the snake.downfunction when downward arrow is hit **
screen.onkey(key="Left", fun=snake.left) #calls the snake.left function when left arrow is hit **
screen.onkey(key="Right", fun=snake.right) #calls the snake.right function when right arrow is hit **




game_is_on = True
while game_is_on:
    screen.update() #when tracer is off, we use update() to tell program to refresh and redraw the screen
    time.sleep(1)  # sleep time is set to 1 second

    snake.move()


#cv
#ry


screen.exitonclick()
