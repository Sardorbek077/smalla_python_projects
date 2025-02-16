import turtle
from turtle import Turtle
from car_manager import COLOURS

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
turtle.colormode(255)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color(COLOURS)
        self.penup()
        self.start()
        self.setheading(90)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(y=new_y, x=0)

    def start(self):
        self.goto(0, -270)

    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


