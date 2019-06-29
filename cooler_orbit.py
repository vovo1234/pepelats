import turtle
import math

wn = turtle.Screen()
wn.bgcolor('black')

zoom = 900

turtle.setworldcoordinates(-zoom, -zoom, zoom, zoom)

x1 = 200
x2 = -200

y1 = 100
y2 = -100

vx1 = 0
vx2 = 0

vy1 = -50
vy2 = 50

ax1 = 0
ax2 = 0

ay1 = 0
ay2 = 0

m1 = 1000000000000
m2 = 1000000000000

a1 = 0
a2 = 0

dt = 1/20

r = 0

G = 6.67408e-11

object1 = turtle.Turtle()
object2 = turtle.Turtle()


object1.shape('circle')
object1.turtlesize(0.25)
object1.color('Dark Slate Blue')
object1.penup()
object1.setpos(x1, y1)
object1.pendown()

object2.shape('circle')
object2.turtlesize(0.25)
object2.color('Cadet Blue')
object2.penup()
object2.setpos(x2, y2)
object2.pendown()

text_writer = turtle.Turtle()
text_writer.hideturtle()
text_writer.color('white')
text_writer.penup()
text_writer.setpos(-800, 800)
text_writer.pendown()
text_writer.setpos(-800, 800)


def tick_update():
    global x1, x2, y1, y2, vx1, vx2, vy1, vy2, ax1, ax2, ay1, ay2, m1, m2, a1, a2, r, dt, G
    r = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    a1 = G * m2 / r * r
    a2 = G * m1 / r * r
    ax1 = a1 * (-x1 - -x2) / r
    ay1 = a1 * (-y1 - -y2) / r
    ax2 = a2 * (x1 - x2) / r
    ay2 = a2 * (y1 - y2) / r
    x1 = x1 + vx1 * dt
    x2 = x2 + vx2 * dt
    y1 = y1 + vy1 * dt
    y2 = y2 + vy2 * dt
    vx1 = vx1 + ax1 * dt
    vx2 = vx2 + ax2 * dt
    vy1 = vy1 + ay1 * dt
    vy2 = vy2 + ay2 * dt
    object1.setpos(x1, y1)
    object2.setpos(x2, y2)
    v1 = math.sqrt(vx1 * vx1 + vy1 * vy1)
    v2 = math.sqrt(vx2 * vx2 + vy2 * vy2)
    text_writer.undo()
    text_writer.write('purples velocity: %s \n blues velocity: %s' % (v1, v2), font=("Comic Sans MS", 10, "normal"))
    turtle.ontimer(tick_update, int(dt * 1000))


tick_update()

turtle.mainloop()
