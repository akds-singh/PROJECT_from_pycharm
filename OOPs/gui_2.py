# Draw Polygons upto 10 sides
from turtle import Turtle, Screen

t1 = Turtle()
color_list = ['gold', "medium spring green", 'chocolate', 'medium violet red', 'violet', 'bisque', 'dark salmon',
              'saddle brown',
              'sandy brown', 'light sky blue', ' navy']
# side = 5
position = 0
for side in range(3, 11):
    angle = 360 / side
    for _ in range(side):
        t1.pencolor(color_list[position])
        t1.forward(100)
        t1.right(angle)
    position += 1
Screen().exitonclick()
