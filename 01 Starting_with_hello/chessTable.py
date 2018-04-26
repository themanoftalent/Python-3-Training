import turtle
turtle.speed("fastest")
side = 40
x = 0
y = 0
for i in range(16):
    for j in range(4):
        if i % 2 == 0:
            turtle.begin_fill()
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.end_fill()
        turtle.forward(side)
    turtle.penup()
    x += 80
    if x == (8*side):
        y += 80
        x = 0
    turtle.goto(x, y)
    turtle.pendown()

turtle.exitonclick()
