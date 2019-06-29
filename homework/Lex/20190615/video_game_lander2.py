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
dt=1/20
angle0=0
velocity0=50
ground_level=-200
is_started=False


body=turtle.Turtle()
body.shape('circle')
body.color('red')
bts = body.turtlesize()
print(bts)

aimbot =turtle.Turtle()
def  draw_aim():
     global angle0, velocity0, aimbot
     aimbot.up()
     aimbot.setpos(x0,y0)
     aimbot.down()
     aimbot.setheading(angle0)
     aimbot.forward(velocity0)
     

text_writer= turtle.Turtle()
text_writer.up()
text_writer.setpos(-200, 200)
text_writer.down()
text_writer.hideturtle()
text_writer.write('stats')

def start():
    global is_started
    if is_started:
        is_started = False
    else:
        is_started=True
        
    
def do_step():
    global x, y, vx, vy, ax, ay, dt, body
    x=x+vx*dt
    y=y+vy*dt
    vx=vx+ax*dt
    vy=vy+ay*dt
    if y<=ground_level+10:
        vy= -vy		
    body.up()

def update():
    global x,y,dt
    if is_started:
        do_step()
    body.setpos(x,y)
    turtle.ontimer(update,int(dt*1000))
    #text_writer.up()
    #text_writer.setpos()
    text_writer.undo()
    text_writer.write(f' x={x} y={y}\n vx={vx} vy={vy}')
    
    
    

update()

def return_back():
	global x0,y0,x,y,vx0,vy0,vx,vy,ax0,ay0,ax,ay
	x=x0
	y=y0
	vx=vx0
	vy=vy0
	ax=ax0
	ay=ay0
	
def draw_ground():
    for i in range(-20, 21):
        x=i*20
        turtle.up()
        turtle.setpos (x,ground_level)
        turtle.down()
        turtle.forward(5)
        turtle.up()
        turtle.setpos (x-10,ground_level-20)
        turtle.down()
        turtle.write(x)
    turtle.up()
    turtle.setpos(-1000,ground_level)
    turtle.down()
    turtle.color('green')
    turtle.begin_fill()
    turtle.setpos(1000, ground_level)
    turtle.end_fill()
    
def angle_plus():
    global angle0, velocity0, aimbot
    angle0=angle0+5
    aimbot.undo()
    draw_aim()
    
def angle_minus():
    global angle0, velocity0, aimbot
    angle0=angle0-5
    aimbot.undo()
    draw_aim()

turtle.onkeypress( start, 'space')	
turtle.onkeypress( return_back,'r')
turtle.onkeypress(angle_plus, "Right")
turtle.onkeypress(angle_minus, "Left")
turtle.listen( )

draw_ground()
draw_aim()
turtle.mainloop()
