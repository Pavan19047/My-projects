import turtle
import turtle as t
import random

tim = t.Turtle()
screen = turtle.Screen()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    generate_color = (r, g, b)
    return generate_color

directions = [0, 90, 180, 270]

tim.width(15)
tim.speed('fastest')
for _ in range(200):
    tim.color(random_color())
    tim.fd(50)
    tim.setheading(random.choice(directions))

screen.exitonclick()
