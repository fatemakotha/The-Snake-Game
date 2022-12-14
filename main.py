from turtle import Turtle, Screen
import time #imports the time module
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600) #screen' width and height set to 600pixels
screen.bgcolor("black") #screen's bgcolor set to black
screen.title("SNAKE GAME") #set title for the screen
screen.tracer(0) #tracer takes a number as input and it turns the animation on/off 0 = off, 1 = on


snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen() #starts listening
screen.onkey(key="Up", fun=snake.up) #calls the snake.up function when upward arrow is hit **
screen.onkey(key="Down", fun=snake.down) #calls the snake.downfunction when downward arrow is hit **
screen.onkey(key="Left", fun=snake.left) #calls the snake.left function when left arrow is hit **
screen.onkey(key="Right", fun=snake.right) #calls the snake.right function when right arrow is hit **




game_is_on = True
while game_is_on:
    screen.update() #when tracer is off, we use update() to tell program to refresh and redraw the screen
    time.sleep(0.1)  # sleep time is set to 1 second
    snake.move()

    #Detect collision with food:
    if snake.head.distance(food) < 15: #distance of snake's head from food is less than 15
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detection collision with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail:
    for segment in snake.segments[1:]: #checks for segments after the head, do checks the body and body and tail
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
