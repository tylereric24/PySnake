from snake import Snake
from turtle import *
from food import Food
from scoreboard import Scoreboard
import time
from playsound import playsound

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
corvals = [(0, 0), (-20, 0), (-40, 0)]
my_turtles = []

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
playsound("theme.mp3", False)
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        playsound("chomp.mp3", False)
        snake.grow()

    #detect wall collision
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_on = False
        #playsound("/Users/erictyler/Snake Game/RIPBOZO.mp3", False)
        score.game_over()

    #detect tail collision
    for snakes in snake.my_turtles[1::1]:
        if snake.head.distance(snakes) < 10:
            game_on = False
            #playsound("/Users/erictyler/Snake Game/RIPBOZO.mp3", False)
            score.game_over()
            
        
screen.exitonclick()