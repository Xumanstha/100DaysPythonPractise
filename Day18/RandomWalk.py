from turtle import Turtle, Screen
import random

def Random_Colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)

tim=Turtle()

new_screen=Screen()
new_screen.colormode(255)
# colors=["red","green","blue","yellow","cyan","magenta","orange","purple"]
directions=[0,90,180,270]
# tim.speed(1)
tim.width(5)
# timmy.speed(1)
# timmy.width(5)
tim.pencolor(Random_Colors())

for _ in range(1000):
    tim.forward(30)
    # timmy.forward(30)
    tim.setheading(random.choice(directions))
    # timmy.setheading(random.choice(directions))
    tim.pencolor(Random_Colors())
    # timmy.pencolor(random.choice(colors))

new_screen.exitonclick()