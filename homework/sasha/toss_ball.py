import turtle
import math
turtle.speed(0)
turtle.delay(None)
ground_level = -200
x0 = 0
y0 = 0
x = 0
y = 0
vx = 10
vy = 10
ax = 0
ay = -10
dt = 1/20
angle0 = 0
velocity0 = 50
time_scale = 2
is_started = False
redraw_arrow = False

def draw_land():
    
    turtle.speed(0)
    turtle.up()
    turtle.setpos(-625,ground_level)
    turtle.down()
    turtle.setpos(625,ground_level)
    turtle.right(90)

    for a in range (-30,31):
        x = a*25
        turtle.up()
        turtle.setpos(x,ground_level)
        turtle.down()
        turtle.forward(5)
        turtle.up()
        turtle.setpos(x-10,ground_level-20)
        turtle.down()
        turtle.write(x)

draw_land()
    
   


def start():
    global is_started
    if is_started:
        is_started = False
    else:
        is_started = True

turtle.up()
turtle.setpos(-350,ground_level)
turtle.hideturtle()
lander = turtle.Turtle()
lander.shape('circle')
lander.color('red')

aimbot = turtle.Turtle()
aimbot.speed(0)

def draw_aim():
    global angle0, velocity0, aimbot
    aimbot_angle = angle0
    aimbot.up()
    aimbot.setpos(x0, y0)
    aimbot.down()
    aimbot.setheading(angle0)
    aimbot.forward(velocity0)
    
draw_aim()

text_writer = turtle.Turtle()
text_writer.up()
text_writer.setpos(-200,200)
text_writer.down()
text_writer.hideturtle()
text_writer.write('stats:')

def do_step():
    global x, y, vx, vy, ax, ay, dt
    dt_scaled = dt*time_scale
    x = x + vx * dt_scaled
    y = y + vy * dt_scaled
    vx = vx + ax * dt_scaled
    vy = vy + ay * dt_scaled
    if y <= ground_level+10:
        vy = -vy
        
def update():
    global x, y, dt, aimbot, redraw_arrow, x0, y0, lander
    global vx, vy, angle0, velocity0
    if is_started:
        lander.down()
        do_step()
    else:
        radians = math.radians(angle0)
        vx = velocity0*math.cos(radians) 
        vy = velocity0*math.sin(radians) 
        x = x0
        y = y0
        lander.up()
        
    if redraw_arrow:
        redraw_arrow=False
        aimbot.undo()
        draw_aim()
    lander.setpos(x, y)
    text_writer.undo()
    text_writer.write(f'x = {x} y = {y}\nx velocity = {vx}  y velocity = {vx}\n'
                      f'angle0 = {angle0}\n'
                      f'velocity0 = {velocity0}\n'
                      f'time_scale = {time_scale}')
    turtle.ontimer(update, (int(dt * 1000)))
    

    
    
def faster():
    global velocity0, redraw_arrow
    velocity0+=5
    redraw_arrow=True

def slower():
    global velocity0, redraw_arrow
    velocity0-=5
    redraw_arrow=True

def turn_left():
    global redraw_arrow, angle0, velocity0
    angle0 = angle0 + 3
    redraw_arrow = True
    


def turn_right():
    global redraw_arrow, angle0, velocity0
    angle0 = angle0 - 3
    redraw_arrow = True

def up():
    global y0, redraw_arrow
    y0 = y0 + 5
    redraw_arrow = True
    


def down():
    global y0, redraw_arrow
    y0 = y0 - 5
    redraw_arrow = True



def right():
    global x0, redraw_arrow
    x0 = x0 + 5
    redraw_arrow = True




def left():
    global x0, redraw_arrow
    x0 = x0 - 5
    redraw_arrow = True

    

turtle.onkeypress( turn_right, 'd' )
turtle.onkeypress( turn_left, 'a' )
turtle.onkeypress( start, 'space' )
turtle.onkeypress( slower, 's' )
turtle.onkeypress( faster, 'w' )
turtle.onkeypress( up, 'Up' )
turtle.onkeypress( down, 'Down' )
turtle.onkeypress( right, 'Right' )
turtle.onkeypress( left, 'Left' )
update()
turtle.listen()
turtle.mainloop()
