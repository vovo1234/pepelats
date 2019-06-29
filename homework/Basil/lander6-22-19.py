import turtle

#lander position
x = 0
y = 0
#lander velocity
vx = 20
vy = 0
tmp_vx = vx
tmp_vy = vy
#lander acceleration
ax = 0
ay = -10
#time step
dt = 1/20
ground_level = -250
started = False
angle0 = 0
redraw_arrow = False
velocity0 = 50
x0 = 0
y0 = 0


body = turtle.Turtle()
body.shape('circle')
body.color('red')
text_writer = turtle.Turtle()
text_writer.hideturtle()
mark_drawer = turtle.Turtle()
aim_arrow = turtle.Turtle()


def up():
    global angle0, redraw_arrow
    angle0 += 5
    redraw_arrow = True


def down():
    global angle0, redraw_arrow
    angle0 -= 5
    redraw_arrow = True


def arrow_up():
    global y0, redraw_arrow
    y0 += 5
    redraw_arrow = True


def arrow_down():
    global y0, redraw_arrow
    y0 -= 5
    redraw_arrow = True


def arrow_left():
    global x0, redraw_arrow
    x0 -= 5
    redraw_arrow = True


def arrow_right():
    global x0, redraw_arrow
    x0 += 5
    redraw_arrow = True


def faster():
    global velocity0, redraw_arrow
    velocity0 += 5
    redraw_arrow = True


def slower():
    global velocity0, redraw_arrow
    velocity0 -= 5
    redraw_arrow = True


def draw_aim():
    global angle0, velocity0, x0, y0
    aim_arrow.penup()
    aim_arrow.setpos(x0, y0)
    aim_arrow.pendown()
    aim_arrow.setheading(angle0)
    aim_arrow.forward(velocity0)


def start():
    global started
    if started:
        started = False
    else:
        started = True


def draw_ground():
    mark_drawer.penup()
    mark_drawer.setpos(-310, -250)
    mark_drawer.pendown()
    for g in range(-15, 16):
        marker = g * 30
        mark_drawer.setpos(marker, -250)
        mark_drawer.setpos(marker, -240)
        mark_drawer.write(marker)
        mark_drawer.setpos(marker, -250)


def restart():
    global x, y, vy, vx
    x = 0
    y = 0
    vx = tmp_vx
    vy = tmp_vy
    body.penup()
    body.setpos(x, y)
    body.pendown()


def do_step():
    global x, y, vx, vy, ax, ay, dt, ground_level
    x = x + vx * dt
    y = y + vy * dt
    vx = vx + ax * dt
    vy = vy + ay * dt
    if y <= ground_level:
        vy = -vy


def update():
    global x, y, dt, started, redraw_arrow
    if started is True:
        do_step()
        body.setpos(x, y)
        text_writer.penup()
        text_writer.undo()
        text_writer.penup()
        text_writer.setpos(-275, 250)
        text_writer.write("x: %s, y: %s \nvx: %s, vy: %s" % (x, y, vx, vy), font=("Arial", 12, "normal"))
    if redraw_arrow is True:
        aim_arrow.undo()
        draw_aim()
        redraw_arrow = False
    turtle.ontimer(update, int(dt * 1000))


turtle.onkeypress(restart, 'r')
turtle.onkeypress(start, 'space')
turtle.onkeypress(up, 'w')
turtle.onkeypress(down, 's')
turtle.onkeypress(slower, 'a')
turtle.onkeypress(faster, 'd')
turtle.onkeypress(arrow_up, 'Up')
turtle.onkeypress(arrow_down, 'Down')
turtle.onkeypress(arrow_left, 'Left')
turtle.onkeypress(arrow_right, 'Right')

turtle.listen()

update()

draw_ground()

draw_aim()

turtle.mainloop()
