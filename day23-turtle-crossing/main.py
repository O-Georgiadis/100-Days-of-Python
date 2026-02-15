import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()


    if player.ycor() > FINISH_LINE_Y:
        player.reset_turtle()
        scoreboard.level_up()
        car_manager.car_level_up()

    # Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()