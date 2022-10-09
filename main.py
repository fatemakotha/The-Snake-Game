from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600) #screen' width and height set to 600pixels
screen.bgcolor("black") #screen's bgcolor set to black
screen.title("SNAKE GAME") #set title for the screen

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for each_snake in range(3):
    snake = Turtle("square")
    snake.color("white")
    snake.goto(starting_positions[each_snake]) #turtle.goto() makes the turtle to go to the x and y coordinate thats specified














screen.exitonclick()
