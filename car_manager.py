from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.car()
        self.axis()

    def car(self):
        self.shape("square")
        self.shapesize(1, 2)
        self.up()
        self.color(choice(COLORS))
        self.setheading(180)

    def move(self, speed):
        self.forward(speed)

    def axis(self):
        ycor = randint(-250, 250)
        self.goto(300, ycor)





