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
ground_level=-200


body=turtle.Turtle()
body.shape('circle')
body.color('red')
bts = body.turtlesize()
print(bts)

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
    do_step()
    body.setpos(x,y)
    turtle.ontimer(update,int(dt*1000))

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
    turtle.up()
    turtle.setpos(-1000,ground_level)
    turtle.down()
    turtle.color('green')
    turtle.begin_fill()
    turtle.setpos(1000, ground_level)
    turtle.end_fill()
	
turtle.onkeypress( return_back,'space')
turtle.listen( )

draw_ground()    
turtle.mainloop()
