
import turtle

# body inital position
x0 = 0
y0 = 0

# body inital angle and velocity
angle0 = 0
velocity0 = 50

# body position
x = 0
y = 0

# body velocity
vx = 0
vy = 0

# body acceleration
ax = 0
ay = -10

is_started = False

dt = 0.05

ground_level = -200
shape_size = 10

turtle.speed( 'fastest' )

# Text writer turtle
writer = turtle.Turtle( )
writer.hideturtle( )
writer.up( )
writer.setpos( -200, 200 )
writer.down( )
writer.write( "..." ) # will be undone

# Aim drawer trutle
aimbot = turtle.Turtle( )

body = turtle.Turtle( )
body.shape( "circle" )
body.color( "red" )

def reset( ):
    global x, y, vx, vy
    x = 0
    y = 0
    vx = 20
    vy = 0

def draw_ground( ):
    global ground_level

    # Draw ground
    turtle.up( )
    turtle.setpos( -500, ground_level )
    turtle.down( )
    turtle.setpos( 500, ground_level )
    
    # Draw distance marks
    turtle.speed( 'fastest' )
    turtle.color( 'blue' )
    grid_size = 10
    grid_step = 50
    for n in range( -grid_size, grid_size + 1 ):
        x = n * grid_step
        turtle.up()
        turtle.setpos( x, ground_level - 5 )
        turtle.down()
        turtle.setpos( x, ground_level + 5 )
        turtle.write( x )
        turtle.up()

def draw_aim( ):
    global aimbot, x0, y0, angle0, velocity0
    aimbot.up( )
    aimbot.setpos( x0, y0 )
    aimbot.down( )
    aimbot.setheading( angle0 )
    aimbot.forward( velocity0 )

def dostep( ):
    global x, y, vx, vy
    x = x + vx * dt
    y = y + vy * dt
    vy = vy - 10*dt
    if y < ground_level:
        vy = -vy

def update( ):
    global x, y, body
    if is_started:
        dostep( )
    body.setpos( x, y )
    turtle.ontimer( update, int( dt * 1000 ) )

def update_text( ):
    global x, y, vx, vy, writer
    writer.undo( )
    writer.write( f"x : {x}\n"
                  f"y : {y}\n"
                  f"vy : {vx}\n"
                  f"vy : {vy}\n" )
    turtle.ontimer( update_text, 1000 )

def toggle_start( ):
    global is_started
    if is_started:
        is_started = False
    else:
        is_started = True

reset( )
draw_ground( )
draw_aim( )
update( )
update_text( )

turtle.onkeypress( toggle_start, 'space' )

turtle.listen( )
turtle.mainloop( )

