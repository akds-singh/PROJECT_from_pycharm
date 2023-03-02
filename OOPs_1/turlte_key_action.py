from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def forward():
    t.forward(10)


def backward():
    t.backward(10)


def counter_clockwise():
    t.left(20)


def clockwise():
    t.right(20)


def clear_screen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
screen.onkey(fun=forward, key='w')
screen.onkey(fun=backward, key='s')
screen.onkey(fun=counter_clockwise, key='a')
screen.onkey(fun=clockwise, key='d')
screen.onkey(fun=clear_screen, key='c')



screen.exitonclick()
