import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
y_cor = -100
screen = Screen()
screen.setup(500, 400)

user_color = screen.textinput('Make your bet', prompt='Which turtle will win the race? enter a color: ')

color_list = ['red', 'blue', 'green','purple', 'yellow', 'orange']
all_turtles = []

for _ in range(6):
    new_turtle = Turtle(shape='turtle')
    if user_color == color_list[_]:
        new_turtle.color(color_list[_])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cor)
    new_turtle.color(color_list[_])
    y_cor += 30
    all_turtles.append(new_turtle)

if user_color:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if turtle.pencolor() == user_color:
                print(f"You've won! The {turtle.pencolor()} turtle is the winner")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner")
            is_race_on = False
        rand_distance = random.randint(1, 10)
        turtle.fd(rand_distance)

screen.exitonclick()