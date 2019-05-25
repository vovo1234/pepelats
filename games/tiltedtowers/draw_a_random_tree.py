import turtle, random

def draw_a_random_tree(size, start_x, start_y, speed, color1, color2):
   turtle.speed(speed)
   turtle.penup()
   turtle.goto(start_x, start_y)
   turtle.pendown()
   turtle.left(90)
   turtle.color(color1)
   turtle.forward(size)
   turtle.right(90)
   turtle.color(color2)
   turtle.begin_fill()
   turtle.circle(size)
   turtle.end_fill()
   for x in range(25):
       turtle.penup()
       turtle.goto(random.randint(start_x - size, start_x + size), random.randint(start_y + size, start_y + size * 2))
       turtle.pendown()
       turtle.begin_fill()
       turtle.circle(size / random.randint(2, 5))
       turtle.end_fill()
       turtle.penup()
       turtle.goto(start_x, start_y)
       turtle.left(90)
       turtle.forward(size)
       turtle.right(90)
       turtle.pendown()

draw_a_random_tree( 100, 0, -100, 0, 'black', 'green' )