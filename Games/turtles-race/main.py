from turtle import Turtle, Screen
import random
import pymsgbox

_colors = ["red", "green", "violet", "grey", "orange"]
_turtles = []
_on_race = True
_turtle_bet = None

screen = Screen()
screen.setup(889, 500, startx=.5, starty=.5)
screen.title("Turtles Race!!!")


for i in range(0, 5):
    turtle = Turtle(shape="turtle", visible=False) 
    turtle.penup()
    turtle.color(_colors[i])
    turtle.goto(x=-430, y=(-222) + 100 * i)
    turtle.st()
    _turtles.append(turtle)

_turtle_bet = screen.textinput("Bet for a turtle: Red / Green / Violet / Grey / Orange", "Name of the turtle: ")

while _on_race:
    for turtle in _turtles:
        if turtle.xcor() >= 425:
            _on_race = False
            pymsgbox.alert('The winner was turtle ' + turtle.pencolor() + '. You win! Amazing!', 'WINNER!!!', button='Accept') if _turtle_bet.casefold() == turtle.color()[0].casefold() else pymsgbox.alert('The winner was turtle ' + turtle.pencolor() + '. You loose :(', 'LOOSER!!!', button='Accept')
            break
        random_distance = random.randint(0, min(425-turtle.xcor() + 1, 20))
        turtle.forward(random_distance)

screen.exitonclick()
