import turtle
import random

wn = turtle.Screen()
wn.bgcolor('Sea Green')
wn.title('Survive')

player = turtle.Turtle()
player.color('Pale Goldenrod')
player.shape('circle')
player.turtlesize(2)
player.penup()

bush = turtle.Turtle()
bush.color('Forest Green')
bush.shape('circle')
bush.turtlesize(3)
bush.penup()
bush.setpos(random.randint(-275, 275), random.randint(-275, 275))

water = turtle.Turtle()
water.color('Medium Turquoise')
water.shape('circle')
water.turtlesize(3)
water.penup()
water.setpos(random.randint(-275, 275), random.randint(-275, 275))

stick = turtle.Turtle()
stick.color('brown')
stick.shape('square')
stick.turtlesize(2, 0.25)
stick.penup()
stick.setpos(random.randint(-275, 275), random.randint(-275, 275))

rock = turtle.Turtle()
rock.color('grey')
rock.shape('circle')
rock.turtlesize(0.5)
rock.penup()
rock.setpos(random.randint(-275, 275), random.randint(-275, 275))

fire = turtle.Turtle()
fire.color('yellow')
fire.shape('circle')
fire.penup()
fire.hideturtle()


def up():
    player.setpos(player.xcor(), player.ycor() + 5)


def down():
    player.setpos(player.xcor(), player.ycor() - 5)


def left():
    player.setpos(player.xcor() - 5, player.ycor())


def right():
    player.setpos(player.xcor() + 5, player.ycor())


berries = 0
bush_health = random.randint(1, 5)


def collect_berries():
    global berries, bush_health
    if player.distance(bush) < 50:
        berries += 1
        bush_health -= 1


sticks = 0
stick_health = random.randint(1, 3)


def collect_stick():
    global sticks, stick_health
    if player.distance(stick) < 20:
        sticks += 1
        stick_health -= 1


rocks = 0
rock_health = random.randint(1, 2)


def collect_rock():
    global rocks, rock_health
    if player.distance(rock) < 20:
        rocks += 1
        rock_health -= 1


def eat():
    global food_left, berries
    if berries > 0:
        food_left += 10
        berries -= 1


heat = False


def build_campfire():
    global rocks, sticks, heat, campfire_health
    if rocks >= 2 and sticks >= 2:
        fire.setpos(player.xcor(), player.ycor())
        fire.showturtle()
        heat = True
        sticks -= 2
        rocks -= 2
        campfire_health = 30


food_left = 50
health = 10
hydration = 50
warmth = 50
campfire_health = 0
time = 0


def tick_update():
    global food_left, berries, health, hydration, warmth, bush_health, stick_health, rock_health, campfire_health, heat, time
    food_left -= 1
    hydration -= 1
    time += 1

    if time >= 12:
        wn.bgcolor('Dim Gray')
        warmth -= 1

    if time >= 24:
        time = 0
        wn.bgcolor('Sea Green')

    if heat == True:
        campfire_health -= 1

    if campfire_health <= 0:
        heat == False
        fire.hideturtle()

    if food_left <= 0:
        health -= 1

    if health <= 0:
        turtle.hideturtle()
        turtle.penup()
        turtle.setpos(-110, 0)
        turtle.color('red')
        turtle.write("WASTED", font=("Comic Sans MS", 45, "normal"))

    turtle.undo()
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(-300, 270)
    turtle.write('food left: %s, berries: %s, health: %s, hydration: %s, warmth: %s, sticks: %s, rocks: %s,'
          ' campfire health: %s, time: %s'
          % (food_left, berries,  health, hydration, warmth, sticks,
             rocks, campfire_health, time), font=("Comic Sans MS", 7, "normal"))

    if food_left >= 50:
        food_left = 50

    if player.distance(water) < 50:
        hydration += 2
        warmth -= 1

    if hydration >= 50:
        hydration = 50

    if hydration <= 0:
        health -= 1

    if warmth <= 0:
        health -= 1

    if warmth >= 50:
        warmth = 50

    if player.distance(fire) <= 15 and heat == True:
        warmth += 2

    if stick_health <= 0:
        stick.setpos(random.randint(-275, 275), random.randint(-275, 275))
        stick_health = random.randint(1, 5)

    if bush_health <= 0:
        bush.setpos(random.randint(-275, 275), random.randint(-275, 275))
        bush_health = random.randint(1, 5)

    if rock_health <= 0:
        rock.setpos(random.randint(-275, 275), random.randint(-275, 275))
        rock_health = random.randint(1, 5)

    turtle.ontimer(tick_update, 1000)


turtle.onkeypress(up, 'Up')
turtle.onkeypress(down, 'Down')
turtle.onkeypress(left, 'Left')
turtle.onkeypress(right, 'Right')
turtle.onkeypress(collect_berries, 'b')
turtle.onkeypress(eat, '1')
turtle.onkeypress(collect_stick, 's')
turtle.onkeypress(collect_rock, 'r')
turtle.onkeypress(build_campfire, 'c')

tick_update()

turtle.listen()

turtle.mainloop()