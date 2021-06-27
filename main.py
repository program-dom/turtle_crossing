import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Run")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")

cars_list = []
speed = 5
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    #making cars
    chance = randint(1, 4)
    if chance == 1:
        car = CarManager()
        cars_list.append(car)
    for car in cars_list:
        car.move(speed)

    #detect collision with car
    for car in cars_list:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect if car across finish line
    if player.ycor() > 280:
        scoreboard.update_score()
        speed += 10

    player.finish()



screen.exitonclick()
