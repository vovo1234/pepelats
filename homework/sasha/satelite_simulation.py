import turtle
import math
planet_radius = 6371000
t = 0
zoom = 25
h = turtle.window_height()
w = turtle.window_width()
#coordinates
x = 0
y = planet_radius
#velocity
vx = 11000
vy = 0
#accelaration
ax = 0
ay = -10

dt = 1/20

#speed control === yup lol(;
time_scale = 10000

turtle.setworldcoordinates(-planet_radius*zoom, -planet_radius*zoom*h/w,
                           planet_radius*zoom, planet_radius*zoom*h/w)
orbiter = turtle.Turtle()
orbiter.shape('circle')
orbiter.color('red')

text_writer = turtle.Turtle()

turtle.speed(0)
turtle.hideturtle()
turtle.color('light sky blue')
turtle.up()
turtle.setpos(0, -planet_radius)
turtle.down()
turtle.begin_fill()
turtle.circle(planet_radius)
turtle.end_fill()


def do_step():
    global x, y, vx, vy, ax, ay, dt, t
    dt_scaled = dt*time_scale
    x = x + vx * dt_scaled
    y = y + vy * dt_scaled
    t = t + dt_scaled 
    G = 6.67408e-11
    planet_mass = 5.972e24
    r = math.sqrt(x*x + y*y)
    a = G*planet_mass/(r*r)
    ax = -x/r*a
    ay = -y/r*a
    vx = vx + ax * dt_scaled
    vy = vy + ay * dt_scaled

def update():
    global x, y, dt, orbiter
    global vx, vy, t
    do_step()
    v = math.sqrt(vx*vx + vy*vy)
    orbiter.setpos(x,y)
    text_writer.undo()
    text_writer.write(f'v = {v}\nt = {t}')
    turtle.ontimer(update, (int(dt * 1000)))

update()
    


turtle.mainloop()
