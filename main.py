from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
food = Food()
scoreboard = Scoreboard()

# Setting up the screen dimensions
screen.setup(width=600, height=600)

# Screen background color
screen.bgcolor("black")

# Setting up the screen title
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

# Making the movement commands for our snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_scoreboard()

#detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        #game_is_on = False
        #scoreboard.game_over()

#detecting collision with tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset
            #game_is_on = False
            #scoreboard.update_scoreboard()
            #scoreboard.game_over()

screen.exitonclick()
