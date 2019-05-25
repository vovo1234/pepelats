import turtle
import time

size = int(input())

turtle.speed(0)

start_pos = size * 10 / 2

for n in range(size + 1):
    y = n * 10 - start_pos
    turtle.penup()
    turtle.setpos(-start_pos, y)
    turtle.pendown()
    turtle.setpos(size * 10 - start_pos, y)

for n in range(size + 1):
    x = n * 10 - start_pos
    turtle.penup()
    turtle.setpos(x, -start_pos)
    turtle.pendown()
    turtle.setpos(x, size * 10 - start_pos)

turtle.penup()
turtle.setpos(0, 0)
turtle.pendown()
turtle.left(90)
turtle.forward(start_pos + 20)
turtle.left(135)
turtle.forward(10)
turtle.left(135)
turtle.forward(14)
turtle.left(135)
turtle.forward(10)
turtle.penup()
turtle.setpos(0, 0)
turtle.setpos(20, start_pos + 20)
turtle.pendown()
turtle.write('y')

turtle.penup()
turtle.setpos(0, 0)
turtle.pendown()
turtle.left(-135)
turtle.forward(start_pos + 20)
turtle.left(135)
turtle.forward(10)
turtle.left(135)
turtle.forward(14)
turtle.left(135)
turtle.forward(10)
turtle.penup()
turtle.setpos(0, 0)
turtle.setpos(start_pos + 20, 20)
turtle.pendown()
turtle.write('x')
turtle.hideturtle()

time.sleep(15)
