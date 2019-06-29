import turtle
planet_radius = 6371000

zoom = 2
h = turtle.window_height()
w = turtle.window_width()
#coordinates
x = 0
y = 0
#velocity
vx = 10
vy = 10
#accelaration
ax = 0
ay = -10

dt = 1/20

#speed control yup lol(;
time_scale = 100

turtle.setworldcoordinates(-planet_radius*zoom, -planet_radius*zoom*h/w,
                           planet_radius*zoom, planet_radius*zoom*h/w)


turtle.speed(0)
turtle.color('light sky blue')
turtle.up()
turtle.setpos(0, -planet_radius)
turtle.down()
turtle.begin_fill()
turtle.circle(planet_radius)
turtle.end_fill()

def do_step():
    global x, y, vx, vy, ax, ay, dt
    dt_scaled = dt*time_scale
    G = 6.67408e-11
    planet_mass = 5.972e24
    r = math.sqrt(x*x + y*y)
    a = G*planet_mass/(r*r)
    ax = -x/r*a
    ay = -y/r*a
    x = x + vx * dt_scaled
    y = y + vy * dt_scaled
    vx = vx + ax * dt_scaled
    vy = vy + ay * dt_scaled

turtle.mainloop()
