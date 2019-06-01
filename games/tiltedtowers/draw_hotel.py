import turtle
turtle.speed(0)

def window(size):
    turtle.color('white')
    turtle.begin_fill()
    for x in range(0,4):
      turtle.forward(40*size/100)
      turtle.left(90)
    for x in range(0,4):
      turtle.forward(20*size/100)
      turtle.left(90)
    for x in range(0,2):
      turtle.forward(40*size/100)
      turtle.left(90)
    turtle.end_fill()
    turtle.color('black')
    turtle.begin_fill()
    for x in range(0,4):
      turtle.forward(40*size/100)
      turtle.left(90)
    for x in range(0,4):
      turtle.forward(20*size/100)
      turtle.left(90)
    for x in range(0,2):
      turtle.forward(40*size/100)
      turtle.left(90)
    for x in range(0,4):
      turtle.forward(20*size/100)
      turtle.left(90)
    for x in range(0,4):
      turtle.forward(20*size/100)
      turtle.left(90)
    for x in range(0,4):
      turtle.forward(40*size/100)
      turtle.left(90)
    for x in range(0,4):
      turtle.forward(20*size/100)
      turtle.left(90)
    for x in range(0,2):
      turtle.forward(40*size/100)
      turtle.left(90)
    for x in range(0,4):
      turtle.forward(20*size/100)
      turtle.left(90)
    for x in range(0,4):
      turtle.forward(20*size/100)
      turtle.left(90)

def door(size):
    turtle.color('brown')
    turtle.begin_fill()
    for x in range(0,2):
      turtle.forward(40*size/100)
      turtle.left(90)
      turtle.forward(20*size/100)
      turtle.left(90)
    turtle.end_fill()


size = 100

size_roof = 144 * size / 250

turtle.clear()
turtle.color('blue')
turtle.begin_fill()
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(60*size/100)
turtle.left(90)
turtle.forward(size)
turtle.left(90)
turtle.forward(60*size/100)
turtle.left(90)
turtle.forward(size)
turtle.end_fill()



turtle.color('red')
turtle.begin_fill()
turtle.right(90)
turtle.forward(size/8)
turtle.left(90)
turtle.left(45)
turtle.forward(size_roof)
turtle.left(90)
turtle.forward(size_roof)
turtle.end_fill()

turtle.up()
turtle.left(90)
turtle.forward(20*size/100)
turtle.down()
turtle.right(45)
window(size/2)
turtle.up()
turtle.right(90)
turtle.forward(5*size/100)
turtle.down()
window(size/2)
turtle.up()
turtle.forward(45*size/100)
turtle.left(90)
turtle.forward(size/4)
turtle.down()
window(size/2)
turtle.up()
turtle.right(90)
turtle.forward(5*size/100)
turtle.down()
window(size/2)
turtle.up()
turtle.forward(45*size/100)
turtle.left(90)
turtle.forward(size/4)
turtle.down()
window(size/2)

turtle.up()
turtle.right(90)
turtle.forward(10*size/100)
turtle.left(90)
turtle.forward(10*size/100)
turtle.right(180)
turtle.down()

door(size/2)


