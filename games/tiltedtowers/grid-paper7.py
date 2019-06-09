import turtle
def grid(step, cellnumber):
    x=step*cellnumber/2
    y=step*cellnumber/2
    for loop in range(cellnumber+1):
        turtle.up()
        turtle.setpos(-x, -y)
        turtle.down()
        turtle.setpos( x, -y)
        y=y-step
    x=step*cellnumber/2
    y=step*cellnumber/2
    for loop in range(cellnumber+1):
        turtle.up()
        turtle.setpos( x,y)
        turtle.down()
        turtle.setpos(x, -y)
        x=x-step
grid(20, 6)
