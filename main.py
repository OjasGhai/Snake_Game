import turtle
from snake import Snake
import time
from turtle import Turtle, Screen
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=600, height=600)

my_screen.bgcolor("black")
my_screen.tracer(0)
my_screen.title("My snake game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()
snake.createsnake()
my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")






game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 13:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.end_game()

    for segment in snake.turtles[1:]:

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.end_game()








my_screen.exitonclick()



