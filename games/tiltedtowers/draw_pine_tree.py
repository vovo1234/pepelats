
import turtle

def draw_pine_tree (size, start_x, start_y, speed, trunk_color, needles_color):
   turn_number = 135
   turtle.speed(speed)
   turtle.penup()
   turtle.goto(start_x, start_y)
   turtle.pendown()
   turtle.left(90)
   turtle.color(trunk_color)
   turtle.forward(size)
   turtle.right(90)
   turtle.color(needles_color)
   turtle.begin_fill()
   turtle.forward(size)
   turtle.left(turn_number)
   turtle.forward(size)
   turtle.right(turn_number)
   turtle.forward(size/2)
   turtle.left(turn_number)
   turtle.forward(size + size/10)
   turtle.left(90)
   turtle.forward(size + size/10)
   turtle.left(turn_number)
   turtle.forward(size/2)
   turtle.right(turn_number)
   turtle.forward(size)
   turtle.left(turn_number)
   turtle.forward(size)
   turtle.end_fill()

draw_pine_tree( 150, 0, -200, 0, 'brown', 'blue' )
