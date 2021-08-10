#Turtle Racing Bet game
#A simple python game/simulation
#Where you can choose a color, and
#see if your turtle will get lucky.
#built using the turtle.py module.

from turtle import Turtle, Screen, color
import random

screen = Screen()
screen.setup(width=500, height=500)

raceison = False

user_bet = screen.textinput(title='Make your bet!',prompt='What turtle do you wanna bet on?(rainbow colors!)')

turtles = []

colors = ["red", 'blue', 'green', 'yellow', 'purple', 'orange']
ypositions = [-75, -50, -25, 0, 25, 50]

for i in range(0,6):   
        new_turtle = Turtle('turtle')
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=(ypositions[i]))
        turtles.append(new_turtle)    
if user_bet:
    raceison = True
while raceison:
    
    for i in turtles:
        randomdistance = random.randint(0, 10)
        i.forward(randomdistance)
        if i.xcor() >= 230:
            winnining_turtle = i.pencolor()
            if user_bet == winnining_turtle:
                print(f'You win!! The winning turtle was the {winnining_turtle} one!')
                raceison = False
            else:
                print(f"No luck today my friend! The winning turtle was the {winnining_turtle} one!")
                raceison = False

screen.exitonclick()