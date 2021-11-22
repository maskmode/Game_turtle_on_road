from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        chance = random.randint(1, 9)
        if chance == 4:
            new_car = Turtle("square")
            new_car.shapesize(1, 3)
            new_car.up()
            new_car.color(random.choice(COLORS))
            randy = random.randrange(-250, 250, 10)
            new_car.goto(300, randy)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level(self):
        self.speed += MOVE_INCREMENT





    #     super().__init__()
    #     self.shape("square")
    #     self.up()
    #     self.color(random.choice(COLORS))
    #     self.shapesize(1, 5)
    #
    # def traffic(self):
    #     self.goto(300, random.randrange(-300, 300, 20))
    #     newx = self.xcor()
    #     while self.xcor() > -300:
    #         newx -= MOVE_INCREMENT
    #         self.goto(newx, self.ycor())
