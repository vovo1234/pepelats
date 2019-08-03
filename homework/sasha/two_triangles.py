import turtle
import sys

x = 0
y = 0

x = int(input('please enter x:'))
y = int(input('please enter y:'))

for k in range(-10,11):
    turtle.setpos(k*x,k*y)
    turtle.setpos(k*x,0)
    turtle.setpos(0,0)
