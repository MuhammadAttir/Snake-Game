import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("The Snake Game")

snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_on=True
while game_on:
    
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Boundry Collison
    if snake.head.xcor()>290 or snake.head.ycor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290:
        game_on = False
        score.Game_Over()
        
    # Food Move and Grow
    if snake.head.distance(food)<14:
        food.refresh()
        score.increase_score()
        snake.add_segment()
    
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_on=False
            score.Game_Over()
            
screen.exitonclick()
