from turtle import Turtle, Screen
import random

t = Turtle()


def turtle_random_move():
    def random_turn():
        num = random.randint(1, 4)
        if num == 1:
            return t.right(90)
        if num == 2:
            return t.left(90)
        if num == 3:
            return t.back(10)

    def random_color():
        r = round(random.random(), 2)
        g = round(random.random(), 2)
        b = round(random.random(), 2)
        return r, g, b

    # color_list = ['gold', "medium spring green", 'chocolate', 'medium violet red', 'violet', 'bisque', 'dark salmon',
    #                   'saddle brown',
    #                   'sandy brown', 'light sky blue', 'navy']

    # 1. make the turtle pen thick
    t.width(5)

    # 2. choose a random  a color

    rand_color = random_color()
    t.pencolor(rand_color)

    # 3. move the turtle forward
    t.speed('fastest')
    t.forward(10)

    # 4. turn either left, right, or back
    random_turn()


# Calling function turtle_random_move several times:
for _ in range(1000):
    turtle_random_move()

Screen().exitonclick()
