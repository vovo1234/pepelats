import turtle

turtle.speed('fastest')

#lander initial position
x0=0
y0=0
#lander position
x=0
y=0
#lander initial velocity 7 angle
angle0 = 0
velocity0 = 50
#vx0=10
#vy0=0
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

#Other variables
is_running = False

aimbot = turtle.Turtle()

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
    if is_running == True:
        do_step()
    body.setpos(x,y)
    turtle.ontimer(update,int(dt*1000))

def onspace():
    global x, y, vy
    x = y = 0
    vy = 0

def drawground():
    # draw ground line
    turtle.color("green")
    global ground_level
    turtle.penup()
    turtle.setpos(-500, ground_level)
    turtle.pendown()
    turtle.setpos(500, ground_level)
    turtle.penup()

    # draw marks
    ruler_x = -500
    ruler_y = ground_level

    while ruler_x - 500:
        turtle.setpos (ruler_x, ruler_y)
        turtle.pendown()
        turtle.setpos(ruler_x, ruler_y - 10)
        turtle.write(ruler_x)
        turtle.penup()
        ruler_x = ruler_x + 50

def pause():
    global is_running
    if is_running == True:
        is_running = False
    else:
        is_running = True

def draw_aim():
    global x0, y0, angle0, velocity0
    aimbot.up()
    aimbot.setpos(x0, y0)
    aimbot.down()
    aimbot.setheading(angle0)
    aimbot.forward(velocity0)

def increase_angle():
    turtle.onkeypress(None, 'Up') #Disable more calls while running
    global angle0, aimbot, x0, y0, angle0, velocity0
    angle0 = angle0 + 10
    aimbot.undo()
    draw_aim()

    turtle.onkeypress(increase_angle, 'Up') #Renable more calls once finished

def decrease_angle():
    turtle.onkeypress(None, 'Down') #Disable more calls while running
    global angle0, aimbot, x0, y0, angle0, velocity0
    angle0 = angle0 - 10
    aimbot.undo()
    draw_aim()

    turtle.onkeypress(decrease_angle, 'Down') #Renable more calls once finished

drawground()
draw_aim()
update()

# The turtle.py for Python 2.7 only defines onkey() -- the onkeypress() variant was added in Python 3
# (as was a synonym for onkey() called onkeyrelease())
turtle.onkeypress(pause, 'space' )
turtle.onkeypress(increase_angle, 'Up' )
turtle.onkeypress(decrease_angle, 'Down' )

turtle.listen( )

turtle.mainloop()