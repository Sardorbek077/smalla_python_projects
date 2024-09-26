import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape('turtle')

tim.speed(0)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_tuple = (red, green, blue)
    return tuple(color_tuple)


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.left(size_of_gap)


def draw_star(num_dot):
    for i in range(num_dot):
        for dot in range(num_dot):
            t.dot(10, (random_color()))
            t.up()
            t.forward(30)

        t.left(135)


def draw_labyrinth(num_dot):
    for i in range(num_dot):
        for dot in range(i):
            t.dot(10, (random_color()))
            t.up()
            t.forward(30)
        t.left(90)


screen = t.Screen()
screen.exitonclick()


