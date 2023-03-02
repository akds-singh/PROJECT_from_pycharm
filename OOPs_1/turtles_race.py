import random
from turtle import Turtle, Screen


def random_move(t):
    """random move by a turtle object"""
    dis = random.randint(1, 10)
    t.forward(dis)


def check_user_guess(guess, win_turtle):
    """check if user guess is right or wrong """
    if guess == win_turtle:
        print(f"Congratulation! Your Guessed turtle color {guess} is right")
    else:
        print(f"Oh no! Your guessed turtle color {guess} is wrong")


screen = Screen()
screen.setup(width=1000, height=600)
colors = ['red', 'blue', 'green', 'yellow', 'magenta']

user_guess = screen.textinput(title='Bets for turtles', prompt='guess which turtle is going to win?')

# Create 5 turtle object and place them at the begging of the line and,
# then append them in a list called 'turtles_list':
sep = 0
turtles_list = []
for index in range(5):
    tur = Turtle(shape='turtle')
    tur.penup()
    turtles_list.append(tur)
    # print(tur)
    tur.goto(x=-490, y=-150 + sep)
    tur.color(colors[index])
    sep += 75

# print(turtles_list)
# Move each turtle to a random distance forward until either one of them is reach the finish line:
not_finish = True
winner = ''
while not_finish:
    for i in range(len(turtles_list)):
        tur = turtles_list[i]
        random_move(tur)
        x_coordinate = tur.xcor()
        if x_coordinate > 480:
            winner = tur
            not_finish = False
            break
        # print(f'tur{i} {x_coordinate}')

pen_color, tur_color = winner.color()   # getting winner turtle's color

# Printing out the winner turtle color and check if my guess turtle color is wright or wrongL
print(f'winner is turtle of color {tur_color}')
check_user_guess(guess=user_guess, win_turtle=tur_color)

screen.exitonclick()
