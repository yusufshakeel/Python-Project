#goto


import turtle
turtle.showturtle()
turtle.color('red')

for i in range(4):
    turtle.forward(30)
    turtle.goto((30 * (i + 1)), (i+1)*30)


turtle.goto(0,0)
