from turtle import Turtle, Screen
import colorgram
import random

colors = colorgram.extract("pic_sample.jpg", 30)

list_of_colors = []
for i in range(len(colors)):
    list_of_colors.append(colors[i].rgb)

t = Turtle()
Screen().colormode(255)
t.hideturtle()
t.speed('fastest')

# goto at position co-ordinate (-200, -200)
t.penup()
t.goto(-200, -200)

# Now draw the dots on the screen:
for i in range(10):
    for j in range(10):
        t.dot(20, random.choice(list_of_colors))
        t.forward(50)

    current_y_coordinate = t.ycor()
    t.goto(-200, current_y_coordinate + 50)

Screen().exitonclick()
