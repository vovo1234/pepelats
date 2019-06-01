import turtle
import time
import town
from town import *

size = 10

turtle.speed(0)

turtle.tracer( False )

draw_field( )

w2s = world_to_screen

turtle.color('black')

start_pos = size * 10 / 2

for n in range(size + 1):
    y = n * 10 - start_pos
    turtle.penup()
    turtle.setpos(w2s(-start_pos, y))
    turtle.pendown()
    turtle.setpos(w2s(size * 10 - start_pos, y))

for n in range(size + 1):
    x = n * 10 - start_pos
    turtle.penup()
    turtle.setpos(w2s(x, -start_pos))
    turtle.pendown()
    turtle.setpos(w2s(x, size * 10 - start_pos))

turtle.penup()
turtle.setpos(w2s(0, 0))
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
turtle.setpos(w2s(0, 0))
turtle.setpos(w2s(20, start_pos + 20))
turtle.pendown()
turtle.write('y')

turtle.penup()
turtle.setpos(w2s(0, 0))
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
turtle.setpos(w2s(0, 0))
turtle.setpos(w2s(start_pos + 20, 20))
turtle.pendown()
turtle.write('x')
turtle.hideturtle()

turtle.mainloop( )
