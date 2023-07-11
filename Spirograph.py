import turtle
import turtle as t
import random

tim = t.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
tim.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    generate_color = (r, g, b)
    return generate_color


for _ in range(100):
    tim.color(random_color())
    radius = 100
    tim.circle(radius)
    tim.left(10)
    tim.circle(radius)
screen.exitonclick()
