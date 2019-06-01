
import turtle

def DrawCar(size, start_x, start_y):

    # increase speed
    turtle.speed(1000)
    # move to starting point
    turtle.penup()
    turtle.goto(start_x, start_y)
    
    # calculate scale
    k = 1.*size/240

    # Make wheel
    turtle.color('black')
    turtle.begin_fill()
    turtle.left (90)
    turtle.circle (k*25, 540)
    turtle.end_fill()

    # make car body
    turtle.color('green')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(k*40)
    turtle.right(90)
    turtle.forward(k*60)
    turtle.right(90)
    turtle.forward(k*70)
    turtle.left(90)
    turtle.forward(k*70)
    turtle.right(90)
    turtle.forward(k*100)
    turtle.right(90)
    turtle.forward(k*70)
    turtle.left(90)
    turtle.forward(k*70)
    turtle.right(90)
    turtle.forward(k*60)
    turtle.right(90)
    turtle.forward(k*40)
    turtle.end_fill()

    # Make wheel 2
    turtle.color('black')
    turtle.begin_fill()
    turtle.right(90)
    turtle.circle(k*25, 540)
    turtle.end_fill()

    # connect wheels
    turtle.right(90)
    turtle.forward(k*60)
    turtle.right(180)

DrawCar(50, 100, 100)
DrawCar(150, 200, 200)
