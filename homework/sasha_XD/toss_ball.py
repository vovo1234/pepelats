import turtle
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
is_started = False
aimbot_angle = angle0

def draw_land():
    
    turtle.speed(0)
    turtle.up()
    turtle.setpos(-350,ground_level)
    turtle.down()
    turtle.setpos(350,ground_level)
    turtle.right(90)

    for a in range (-15,16):
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

def left():
    global aimbot, angle0, velocity0
    angle0 = angle0 + 1

def right():
    global aimbot, angle0, velocity0
    angle0 = angle0 - 1

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
    global angle0, velocity0, aimbot, aimbot_angle
    aimbot_angle = angle0
    aimbot.up()
    aimbot.setpos(x0, y0)
    aimbot.down()
    aimbot.setheading(aimbot_angle)
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
    x = x + vx * dt
    y = y + vy * dt
    vx = vx + ax * dt
    vy = vy + ay * dt
    if y <= ground_level+10:
        vy = -vy
        
def update():
    global x, y, dt, aimbot
    if is_started:
        do_step()
    if not angle0 == aimbot_angle:
        aimbot.undo()
        draw_aim()
    lander.setpos(x, y)
    text_writer.undo()
    text_writer.write(f'x = {x} y = {y}\nx velocity = {vx}  y velocity = {vy}')
    turtle.ontimer(update, (int(dt * 1000)))
    

    
    
def reset():
    global x, y, vx, vy
    x=0
    y=0
    vx=10
    vy=10
    lander.up()
    lander.setpos(0,0)
    lander.down()

turtle.onkeypress( right, 'Right' )
turtle.onkeypress( left, 'Left' )
turtle.onkeypress( start, 'space' )
turtle.onkeypress( reset, 'r' )
update()
turtle.listen()
turtle.mainloop()
