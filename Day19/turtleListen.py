from turtle import Turtle, Screen

tim=Turtle()

angle=5

screen=Screen()


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_right():
    new_heading=tim.heading()-10
    tim.setheading(new_heading)

def move_left():
    new_heading=tim.heading()+10
    tim.setheading(new_heading)

def Reset():
    tim.reset()
    
tim.teleport(0,-220)
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="d",fun=move_right)
screen.onkey(key="a",fun=move_left)
screen.onkey(key="c",fun=Reset)
# times=360/angle
# while angle<15:
#     for i in range(int(times)):
#         move_forward()
#         move_left()
#     angle=angle+1
#     times=360/angle

screen.exitonclick()

