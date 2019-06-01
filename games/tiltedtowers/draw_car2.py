import turtle

def DrawCar(size, start_x, start_y):
# increase speed
    turtle.speed(1000)

    # Make wheel
    turtle.color('black')
    turtle.begin_fill()
    turtle.left (90)
    turtle.circle (25, 540)
    turtle.end_fill()

    # make car body
    turtle.color('green')
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward (40)
    turtle.right (90)
    turtle.forward (60)
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(70)
    turtle.left(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(40)
    turtle.end_fill()

    # Make wheel 2
    turtle.color('black')
    turtle.begin_fill()
    turtle.right(90)
    turtle.circle(25, 540)
    turtle.end_fill()

    # connect wheels
    turtle.right(90)
    turtle.forward(60)

DrawCar(100, 100, 100)





