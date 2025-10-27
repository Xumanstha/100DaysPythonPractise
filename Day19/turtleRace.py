from turtle import Turtle,Screen
import random

screen=Screen()
turtles=[]
screen.setup(width=800,height=400)
colors=["red","green","yellow","orange","blue","purple"]
user_bet=screen.textinput(title="Place your bet",prompt="Which turtle will win the race? Enter a color.")

i=0
for color in colors:
    new_turtle=Turtle()
    new_turtle.color(color)
    new_turtle.shape("turtle")
    new_turtle.penup()
    i=i+1
    new_turtle.goto(-370,-120+i*50)
    turtles.append(new_turtle)

winner=""
if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in turtles:
        move=random.randint(0,10)
        turtle.speed(3)
        turtle.forward(move)
        pos=turtle.position()
        if turtle.xcor()>=370:
            is_race_on=False
            winner=turtle.color()[0]
            break

print(f"The winner color is {winner}")

screen.exitonclick()