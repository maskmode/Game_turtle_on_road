import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(player.go_up, "Up")

sleep_time = 0.1
game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_car()

    # Detect DTP
    for i in car.all_cars:
        if i.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful
    if player.finish_line():
        player.go_start()
        car.level()
        scoreboard.hlevel()




screen.exitonclick()