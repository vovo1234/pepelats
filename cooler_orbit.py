import turtle
import math

wn = turtle.Screen()
wn.bgcolor('black')

zoom = 3000

turtle.setworldcoordinates(-zoom, -zoom, zoom, zoom)

x1 = 2270
x2 = -2270

y1 = 2070
y2 = 2270

vx1 = 0
vx2 = 0

vy1 = 2
vy2 = -2

ax1 = 0
ax2 = 0

ay1 = 0
ay2 = 0

m1 = 1000000000
m2 = 10000000000

a1 = 0
a2 = 0

r = 0

dt = 1/20

G = 6.67408e-11

object1 = turtle.Turtle()
object2 = turtle.Turtle()


object1.shape('circle')
object1.turtlesize(0.15)
object1.color('Dark Slate Blue')
object1.penup()
object1.setpos(x1, y1)
object1.pendown()

object2.shape('circle')
object2.turtlesize(0.15)
object2.color('Cadet Blue')
object2.penup()
object2.setpos(x2, y2)
object2.pendown()


def tick_update():
    global x1, x2, y1, y2, vx1, vx2, vy1, vy2, ax1, ax2, ay1, ay2, m1, m2, a1, a2, r, dt, G
    r = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    a1 = G * m2 / r * r
    a2 = G * m1 / r * r
    ax1 = a1 * (-x1 - -x2) / r
    ay1 = a1 * (-y1 - -y2) / r
    ax2 = a2 * (x1 - x2) / r
    ay2 = a2 * (y1 - y2) / r
    x1 = x1 + vx1
    x2 = x2 + vx2
    y1 = y1 + vy1
    y2 = y2 + vy2
    vx1 = vx1 + ax1
    vx2 = vx2 + ax2
    vy1 = vy1 + ay1
    vy2 = vy2 + ay2
    object1.setpos(x1, y1)
    object2.setpos(x2, y2)
    turtle.ontimer(tick_update, int(dt / 1000000000000000000))


tick_update()

turtle.mainloop()
