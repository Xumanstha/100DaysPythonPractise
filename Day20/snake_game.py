from turtle import Turtle,Screen

def move_upward():
    timmy.setheading(90)

def move_downward():
    timmy.setheading(270)

def move_east():
    timmy.setheading(0)

def move_west():
    timmy.setheading(180)

segment1=Turtle()
segment2=Turtle()
segment3=Turtle()
screen=Screen()

segment1.shape("square")
segment2.shape("square")
segment3.shape("square")

segment2.teleport(-20,0)
segment3.teleport(-40,0)

print(f"{screen.window_height()}*{screen.window_width()}")

is_game_on=True

segment1.penup()
segment2.penup()
segment3.penup()

screen.listen()
while is_game_on:
    segment1.speed(1)
    segment1.forward(10)
    segment2.speed(1)
    segment2.goto(segment1.xcor()-20,0)
    segment3.speed(1)
    segment3.goto(segment1.xcor()-40,0)

    print(f"x_coordinate={segment1.xcor()} and y_coordinate={segment1.ycor()}") 
    screen.onkey(key="w",fun=move_upward)
    screen.onkey(key="a",fun=move_west)
    screen.onkey(key="d",fun=move_east)
    screen.onkey(key="s",fun=move_downward)
    if abs(segment1.xcor())>=320 or abs(segment1.ycor())>=270:
        is_game_on=False
    

screen.exitonclick()

