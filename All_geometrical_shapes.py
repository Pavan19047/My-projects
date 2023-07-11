from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.color("red")
tim.fd(100)
tim.right(120)
tim.fd(100)  # Triangle
tim.right(120)
tim.fd(100)
tim.right(120)
tim.fd(100)

tim.color("NavyBlue")
tim.right(90)
tim.fd(110)
tim.right(90)  # Square
tim.fd(100)
tim.right(90)
tim.fd(110)
tim.right(90)

tim.color("magenta")
for i in range(5):
    tim.forward(100)           # Pentagon
    tim.right(72)

tim.color("violet")
for i in range(6):
    tim.forward(100)            # Hexagon
    tim.right(60)

tim.color("purple")
for i in range(7):
    tim.forward(100)            # Heptagon
    tim.right(51.4)

tim.color("yellow1")
for i in range(8):
    tim.forward(100)            # Octagon
    tim.right(45)

tim.color("GreenYellow")
for i in range(9):
    tim.forward(100)            # Nonagon
    tim.right(40)

tim.color("firebrick")
for i in range(10):
    tim.forward(100)            # Decagon
    tim.right(36)

screen.exitonclick()
