from turtle import Turtle,Screen
timmy=Turtle()
new_Screen=Screen()
timmy.shape("arrow")
timmy.width(5)
timmy.teleport(0,-60)
no_of_sides=3
colors=["red","green","blue","yellow","cyan","magenta","orange","purple"]
j=0
while no_of_sides<11:
    timmy.pencolor(colors[j])
    sum_of_interior_angles=(no_of_sides-2)*180
    interior_angle=sum_of_interior_angles/no_of_sides
    for i in range(no_of_sides):
        timmy.forward(100)
        timmy.left(180-interior_angle)
    no_of_sides+=1
    j+=1

new_Screen.exitonclick()