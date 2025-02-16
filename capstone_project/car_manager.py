import turtle
from turtle import Turtle
import random as r


STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
R = r.randint(0, 255)
G = r.randint(0, 255)
B = r.randint(0, 255)
COLOURS = (R, G, B)
turtle.colormode(255)


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = r.randint(1, 7)
        if random_chance == 1:

            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color((r.randint(0, 255)), r.randint(0, 255), r.randint(0, 255))
            new_car.goto(290, r.randint(-260, 260))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT - 2
