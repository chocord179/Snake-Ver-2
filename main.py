from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import tkinter as tk

parent = tk.Tk() # Create the object
parent.iconbitmap("error.ico") # Set an icon
parent.withdraw() # Hide the window as we do not want to see this one
parent.overrideredirect(1) # Avoid it appearing and then disappearing quickly

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("ERR_GAME_ON")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() <-280:
        game_is_on = False
        error = tk.messagebox.showinfo('ERR_GAME_OVER', 'You lost! Open game to restart!', parent=parent)
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            error = tk.messagebox.showerror('ERR_GAME_OVER', 'You lost! Open game to restart!', parent=parent)
            scoreboard.game_over()