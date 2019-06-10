import turtle
import random
import time as time

wn = turtle.Screen()
wn.bgcolor('Sea Green')
wn.title('Survive')

wn.addshape('player11.gif')
wn.addshape('player21.gif')
wn.addshape('player31.gif')
wn.addshape('player41.gif')

wn.addshape('player12.gif')
wn.addshape('player22.gif')
wn.addshape('player32.gif')
wn.addshape('player42.gif')

wn.addshape('player10.gif')
wn.addshape('player20.gif')
wn.addshape('player30.gif')
wn.addshape('player40.gif')

wn.addshape('player13.gif')
wn.addshape('player23.gif')
wn.addshape('player33.gif')
wn.addshape('player43.gif')

wn.addshape('stick.gif')

wn.addshape('rock.gif')

wn.addshape('pine_tree.gif')

wn.addshape('berry_bush.gif')

wn.addshape('pond.gif')

wn.addshape('zombie1.gif')
wn.addshape('zombie2.gif')
wn.addshape('zombie3.gif')
wn.addshape('zombie4.gif')

wn.addshape('campfire1.gif')
wn.addshape('campfire2.gif')

water = turtle.Turtle()
water.shape('pond.gif')
water.turtlesize(3)
water.penup()
water.setpos(random.randint(-275, 275), random.randint(-275, 275))

bush = turtle.Turtle()
bush.shape('berry_bush.gif')
bush.turtlesize(3)
bush.penup()
bush.setpos(random.randint(-275, 275), random.randint(-275, 275))

stick = turtle.Turtle()
stick.shape('stick.gif')
stick.turtlesize(2, 0.25)
stick.penup()
stick.setpos(random.randint(-275, 275), random.randint(-275, 275))

rock = turtle.Turtle()
rock.shape('rock.gif')
rock.turtlesize(0.5)
rock.penup()
rock.setpos(random.randint(-275, 275), random.randint(-275, 275))

tree = turtle.Turtle()
tree.shape('pine_tree.gif')
tree.turtlesize(3)
tree.penup()
tree.setpos(random.randint(-275, 275), random.randint(-275, 275))

fire = turtle.Turtle()
fire.hideturtle()
fire.shape('campfire1.gif')
fire.penup()

zombie = turtle.Turtle()
zombie.hideturtle()
zombie.shape('circle')
zombie.turtlesize(2)
zombie.penup()
zombie.setpos(random.randint(-275, 275), random.randint(-275, 275))

player = turtle.Turtle()
player.shape('player10.gif')
player.turtlesize(2)
player.penup()

wasted_screen = turtle.Turtle()
wasted_screen.hideturtle()


def up():
    player.shape('player12.gif')
    player.setpos(player.xcor(), player.ycor() + 5)
    player.shape('player11.gif')
    if axe is True:
        player.shape('player13.gif')
    else:
        player.shape('player10.gif')


def down():
    player.shape('player32.gif')
    player.setpos(player.xcor(), player.ycor() - 5)
    player.shape('player31.gif')
    if axe is True:
        player.shape('player33.gif')
    else:
        player.shape('player30.gif')


def left():
    player.shape('player22.gif')
    player.setpos(player.xcor() - 5, player.ycor())
    player.shape('player21.gif')
    if axe is True:
        player.shape('player43.gif')
    else:
        player.shape('player20.gif')


def right():
    player.shape('player42.gif')
    player.setpos(player.xcor() + 5, player.ycor())
    player.shape('player41.gif')
    if axe is True:
        player.shape('player23.gif')
    else:
        player.shape('player40.gif')


berries = 0
bush_health = random.randint(1, 5)


def collect_berries():
    global berries, bush_health
    if player.distance(bush) < 50:
        berries += 1
        bush_health -= 1


wood = 0
stick_health = random.randint(1, 3)


def collect_stick():
    global wood, stick_health
    if player.distance(stick) < 40:
        wood += 1
        stick_health -= 1


rocks = 0
rock_health = random.randint(1, 2)


def collect_rock():
    global rocks, rock_health
    if player.distance(rock) < 20:
        rocks += 1
        rock_health -= 1


def collect_tree():
    global wood, axe
    if player.distance(tree) < 50 and axe is True:
        wood += 2


def eat():
    global food_left, berries
    if berries > 0:
        food_left += 10
        berries -= 1


heat = False


def build_campfire():
    global rocks, wood, heat, campfire_health
    if rocks >= 2 and wood >= 2:
        fire.setpos(player.xcor(), player.ycor())
        fire.showturtle()
        heat = True
        wood -= 2
        rocks -= 2
        campfire_health = 30


axe = False


def craft_axe():
    global rock, wood, axe
    if rocks >= 7 and wood >= 7:
        axe = True


zombie_health = 7


def attack():
    global zombie_health
    if player.distance(zombie) < 40:
        zombie_health -= 1


food_left = 50
health = 10
hydration = 50
warmth = 50
campfire_health = 0
game_time = 0
zombie_attack = False
start = time.time()


def tick_update():
    global food_left, berries, health, hydration, warmth, bush_health, stick_health, rock_health,\
        campfire_health, heat, game_time, zombie_attack, zombie_health
    food_left -= 1
    hydration -= 1
    game_time += 1
    fire.shape('campfire2.gif')

    if zombie_health <= 0:
        zombie_health = 7
        zombie.hideturtle()
        zombie.setpos(random.randint(-275, 275), random.randint(-275, 275))
        zombie.showturtle()

    if game_time >= 12:
        wn.bgcolor('Dim Gray')
        warmth -= 1
        zombie_attack = True
        zombie.showturtle()
        if zombie.ycor() > player.ycor():
            zombie.setpos(zombie.xcor(), zombie.ycor() - 10)
            zombie.shape('zombie3.gif')

        if zombie.ycor() < player.ycor():
            zombie.setpos(zombie.xcor(), zombie.ycor() + 10)
            zombie.shape('zombie1.gif')

        if zombie.xcor() > player.xcor():
            zombie.setpos(zombie.xcor() - 10, zombie.ycor())
            zombie.shape('zombie4.gif')

        if zombie.xcor() < player.xcor():
            zombie.setpos(zombie.xcor() + 10, zombie.ycor())
            zombie.shape('zombie2.gif')
    else:
        zombie.hideturtle()
        zombie_attack = False

    if zombie_attack is True and zombie.distance(player) < 30:
        health -= 1

    if health > 10:
        health = 10

    if food_left >= 45 and hydration >= 45:
        health += 1

    if game_time >= 24:
        game_time = 0
        wn.bgcolor('Sea Green')

    if heat is True:
        campfire_health -= 1

    if campfire_health <= 0:
        heat = False
        campfire_health = 0
        fire.hideturtle()

    if food_left <= 0:
        health -= 1

    if health <= 0:
        wasted_screen.penup()
        wasted_screen.setpos(-110, 0)
        wasted_screen.color('red')
        end = time.time()
        final_time = (end - start) / 24
        wasted_screen.write("WASTED", font=("Arial", 45, "normal"))
        wasted_screen.setpos(-150, -35)
        wasted_screen.write("You Survived For: %s Days" % (final_time), font=("Arial", 15, "normal"))
        time.sleep(10000)

    turtle.undo()
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(-300, 270)
    turtle.write('food left: %s, berries: %s, health: %s, hydration: %s, warmth: %s, wood: %s, rocks: %s,'
          ' campfire health: %s, time: %s'
            % (food_left, berries,  health, hydration, warmth, wood,
            rocks, campfire_health, game_time), font=("Arial", 7, "normal"))

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

    if player.distance(fire) <= 35 and heat is True:
        warmth += 3

    if stick_health <= 0:
        stick.setpos(random.randint(-275, 275), random.randint(-275, 275))
        stick_health = random.randint(1, 5)

    if bush_health <= 0:
        bush.setpos(random.randint(-275, 275), random.randint(-275, 275))
        bush_health = random.randint(1, 5)

    if rock_health <= 0:
        rock.setpos(random.randint(-275, 275), random.randint(-275, 275))
        rock_health = random.randint(1, 5)

    fire.shape('campfire1.gif')

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
turtle.onkeypress(craft_axe, 'a')
turtle.onkeypress(collect_tree, 'w')
turtle.onkeypress(attack, 'space')

tick_update()

turtle.listen()

turtle.mainloop()
