from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
timmy = Turtle()

colors = ["violet", "blue", "yellow", "red", "orange", "green"]
t = []

choice = screen.textinput("TURTLE RACE", "enter your turtle color: violet/blue/yellow/red/orange/green")

for i in range(6):
    t.append(Turtle(shape="turtle"))
    t[-1].color(colors[i])
    t[-1].penup()
    t[-1].setposition(-240, -150 + i*50)

is_on = True

while is_on:
    for i in t:
        i.forward(random.randint(0,30))
        if i.xcor() >= 240:
            is_on = False
            if i.pencolor() == choice:
                screen.title(f"you win, winner is {i.pencolor()}")
            else:
                screen.title(f"you lose, winner is {i.pencolor()}")



screen.exitonclick()
