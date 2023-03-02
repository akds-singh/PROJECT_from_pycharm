from turtle import Turtle, Screen
import random

t1 = Turtle()


def random_color():
    r = round(random.random(), 2)
    g = round(random.random(), 2)
    b = round(random.random(), 2)
    return r, g, b


rc = random_color()
print(rc)

t1.pencolor(rc)
# t1.circle(100, 180)
# t1.home()
# t1.goto(100, 100)
# print(t1.towards(0, 0))
# print(t1.position())
for _ in range(int(360/45)):
    t1.left(45)
    t1.circle(100)

# t1.left(270)
# t1.goto(100, 100)
# print(t1.towards(0,0))

Screen().exitonclick()
