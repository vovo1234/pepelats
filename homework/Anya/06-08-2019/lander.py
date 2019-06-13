import turtle

#lander initial position
x0=0
y0=0
#lander position
x=0
y=0
#lander initial velocity
vx0=10
vy0=0
#lander velocity
vx=10
vy=0
#lander initial acceleration
ax0=0
ay0=-10
#lander acceleration
ax=0
ay=-10
#time step
dt=1./20
ground_level=-200
i=0


body=turtle.Turtle()
body.shape('square')
body.color('purple')
bts = body.turtlesize()
print(bts)

def do_step():
    global x, y, vx, vy, ax, ay, dt, body, i
    x=x+vx*dt
    y=y+vy*dt
    vx=vx+ax*dt
    vy=vy+ay*dt
    if y<=ground_level+10:
        vy= -vy		
    body.up()

def update():
    global x,y,dt
    do_step()
    body.setpos(x,y)
    turtle.ontimer(update,int(dt*1000))

def onspace():
    global x, y, vy
    x = y = 0
    vy = 0

def drawground():
    turtle.color("green")
    global ground_level
    turtle.penup()
    turtle.setpos(-500, ground_level)
    turtle.pendown()
    turtle.setpos(500, ground_level)
    turtle.penup()
    ruler_x = -500
    ruler_y = ground_level

    for i in range(10):
        turtle.setpos (ruler_x, ruler_y)
        turtle.pendown()
        turtle.setpos(ruler_x, ruler_y - 10)
        turtle.penup()
        ruler_x = ruler_x + 50


drawground()
update()

# The turtle.py for Python 2.7 only defines onkey() -- the onkeypress() variant was added in Python 3 (as was a synonym for onkey() called onkeyrelease())
turtle.onkey(onspace, 'space' )

turtle.listen( )

turtle.mainloop()
