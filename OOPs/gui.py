from turtle import Turtle, Screen

t = Turtle()
n=0
while n<10:
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
    # t.forward(10)
    n +=1
Screen().exitonclick()