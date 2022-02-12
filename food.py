from turtle import Turtle
import random as rand

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("brown")
        self.speed("fastest")
        random_x = rand.randint(-280, 280)
        random_y = rand.randint(-280, 280)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = rand.randint(-250, 250)
        random_y = rand.randint(-250, 250)
        self.goto(random_x, random_y)