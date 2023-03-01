from turtle import  Turtle, Screen
import  random


def random_color():
    r = round(random.random(), 2)
    g = round(random.random(), 2)
    b = round(random.random(), 2)
    return r, g, b


t = Turtle()
t.speed('fastest')
angle = 5
for _ in range(int(360/angle)):
    t.pencolor(random_color())
    t.circle(100)
    t.left(angle)

Screen().exitonclick()