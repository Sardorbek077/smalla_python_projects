"""We don't need these codes anymore, because we have already extracted colors"""

# import colorgram
#
# rgb = []
#
# colors = colorgram.extract('image_dot.jpg', 10)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb.append((r, g, b))
# print(rgb)

# color_list = [(251, 25, 154), (252, 248, 252), (239, 134, 35), (92, 192, 246), (250, 239, 49), (162, 201, 31), (1, 38, 79), (125, 5, 187)]


import turtle as t
import random

t.colormode(255)

t.speed(0)


def random_color():
    """This function creates random colour from rgb """
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_tuple = (red, green, blue)
    return tuple(color_tuple)


t.hideturtle()
t.setheading(225)
t.up()
t.forward(300)
t.left(135)


def draw_dot(num_dot):
    for i in range(num_dot):
        for dot in range(num_dot):
            t.dot(10, (random_color()))
            t.forward(30)

        t.left(90)
        t.forward(30)
        t.left(90)
        t.forward(num_dot * 30)
        t.left(180)


draw_dot(20)


screen = t.Screen()
screen.exitonclick()
