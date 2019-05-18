import turtle   #Main Body
def tortoise(l, x, y):
    turtle.up()
    turtle.setpos(l/3.4,l/2.5)
    turtle.down()
    turtle.left(150)
    turtle.color("yellow", "green")
    turtle.begin_fill()
    for loop in range(2):       # Draws 2 halves of ellipse
        turtle.circle(l*0.36,90)   # Long curved part
        turtle.circle(l*0.18,90)   # Short curved part
    turtle.end_fill()
    turtle.circle(l*0.36,90)   #Neck/Head part
    turtle.right(65)
    turtle.color("green", "brown")
    turtle.begin_fill()
    turtle.forward(l*0.09)
    turtle.right(30)
    for loop in range(2):      
        turtle.circle(l*0.18,90)
        turtle.circle(l*0.018,90)
    turtle.end_fill()
    turtle.up()             
    turtle.left(45)
    turtle.forward(l*0.136)
    turtle.down()
    turtle.color("yellow", "black")
    turtle.begin_fill()
    turtle.circle(l*0.018)
    turtle.end_fill()
    turtle.up()             
    turtle.left(20)
    turtle.forward(l*0.118)
    turtle.right(180)
    turtle.down()
    turtle.forward(l*0.09)
    turtle.up()
    turtle.right(45)
    turtle.forward(l*0.127)
    turtle.down()
    turtle.color("green", "brown")
    turtle.begin_fill()
    turtle.forward(l*0.109)
    turtle.left(100)
    turtle.forward(l*0.09)
    turtle.left(90)
    turtle.forward(l*0.09)
    turtle.left(90)
    turtle.up()
    turtle.forward(l*0.076)
    turtle.end_fill()
    turtle.left(90)     #Leg 1
    turtle.forward(l*0.109)
    turtle.right(90)
    turtle.forward(l*0.1)
    turtle.down()
    turtle.color ("green", "brown")
    turtle.begin_fill()
    for loop in range(4):
        turtle.forward(l*0.136)
        turtle.left(90)
    turtle.end_fill()
    turtle.left(90)
    turtle.up()
    turtle.forward(l*0.36)
    turtle.color ("green", "brown")
    turtle.begin_fill()
    for loop in range(4):
        turtle.forward(l*0.136)
        turtle.right(90)
    turtle.end_fill()
    turtle.left(45)
    turtle.up()
    turtle.forward(l*0.27)
    turtle.down()
    turtle.color ("green", "brown")
    turtle.begin_fill()
    for loop in range(3):
        turtle.forward(l*0.136)
        turtle.left(120)
    turtle.end_fill()
        
tortoise(600, 0, 0)















