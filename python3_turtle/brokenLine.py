#broken lines
#using goto penup pendown

import turtle
turtle.showturtle()
turtle.color('red')

for i in range(5):
    turtle.forward(40)
    turtle.penup()
    turtle.goto((i + 1) * 50, 0)
    turtle.pendown()
