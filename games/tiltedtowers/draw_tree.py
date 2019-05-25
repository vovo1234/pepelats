
import turtle
import time


def draw_a_tree(size, start_x, start_y, speed):
   turtle.speed(speed)
   turtle.penup()
   turtle.goto(start_x, start_y)
   turtle.pendown()
   turtle.left(90)
   turtle.color('brown')
   turtle.forward(size)
   turtle.right(90)
   turtle.color('green')
   turtle.begin_fill()
   turtle.circle(size)
   turtle.end_fill()

draw_a_tree( 100, 0, 0, 0 )
