import turtle
import random
import time

window = turtle.Screen()
window.bgcolor('Sea Green')
window.title('dis boiii')

window.addshape('images/player11.gif')
window.addshape('images/player21.gif')
window.addshape('images/player31.gif')
window.addshape('images/player41.gif')

window.addshape('images/player12.gif')
window.addshape('images/player22.gif')
window.addshape('images/player32.gif')
window.addshape('images/player42.gif')

window.addshape('images/player10.gif')
window.addshape('images/player20.gif')
window.addshape('images/player30.gif')
window.addshape('images/player40.gif')

window.addshape('images/player13.gif')
window.addshape('images/player23.gif')
window.addshape('images/player33.gif')
window.addshape('images/player43.gif')

window.addshape('images/stick.gif')

window.addshape('images/rock.gif')

window.addshape('images/pine_tree.gif')

window.addshape('images/berry_bush.gif')

window.addshape('images/pond.gif')

window.addshape('images/zombie1.gif')
window.addshape('images/zombie2.gif')
window.addshape('images/zombie3.gif')
window.addshape('images/zombie4.gif')

window.addshape('images/campfire1.gif')
window.addshape('images/campfire2.gif')

window.addshape('images/dont_copyright_strike_me_plz.gif')

water = turtle.Turtle()
water.shape('images/pond.gif')
water.turtlesize(3)
water.penup()
water.setpos(random.randint(-275, 275), random.randint(-275, 275))

bush = turtle.Turtle()
bush.shape('images/berry_bush.gif')
bush.turtlesize(3)
bush.penup()
bush.setpos(random.randint(-275, 275), random.randint(-275, 275))

stick = turtle.Turtle()
stick.shape('images/stick.gif')
stick.turtlesize(2, 0.25)
stick.penup()
stick.setpos(random.randint(-275, 275), random.randint(-275, 275))

rock = turtle.Turtle()
rock.shape('images/rock.gif')
rock.turtlesize(0.5)
rock.penup()
rock.setpos(random.randint(-275, 275), random.randint(-275, 275))

tree = turtle.Turtle()
tree.shape('images/pine_tree.gif')
tree.turtlesize(3)
tree.penup()
tree.setpos(random.randint(-275, 275), random.randint(-275, 275))

fire = turtle.Turtle()
fire.hideturtle()
fire.shape('images/campfire1.gif')
fire.penup()

zombie = turtle.Turtle()
zombie.hideturtle()
zombie.shape('images/zombie1.gif')
zombie.turtlesize(2)
zombie.penup()
zombie.setpos(random.randint(-275, 275), random.randint(-275, 275))

test_object = turtle.Turtle()
test_object.shape('circle')
test_object.hideturtle()
test_object.penup()

player = turtle.Turtle()
player.shape('images/player10.gif')
player.turtlesize(2)
player.penup()

wasted_screen = turtle.Turtle()
wasted_screen.hideturtle()


def up():
    player.setpos(player.xcor(), player.ycor() + 5)
    player.shape('images/player12.gif')
    player.shape('images/player11.gif')
    if axe is True:
        player.shape('images/player13.gif')
    else:
        player.shape('images/player10.gif')


def down():
    player.setpos(player.xcor(), player.ycor() - 5)
    player.shape('images/player32.gif')
    player.shape('images/player31.gif')
    if axe is True:
        player.shape('images/player33.gif')
    else:
        player.shape('images/player30.gif')


def left():
    player.setpos(player.xcor() - 5, player.ycor())
    player.shape('images/player22.gif')
    player.shape('images/player21.gif')
    if axe is True:
        player.shape('images/player43.gif')
    else:
        player.shape('images/player20.gif')


def right():
    player.setpos(player.xcor() + 5, player.ycor())
    player.shape('images/player42.gif')
    player.shape('images/player41.gif')
    if axe is True:
        player.shape('images/player23.gif')
    else:
        player.shape('images/player40.gif')


bush_health = random.randint(1, 5)
zombie_health = 7
wood = 0
stick_health = random.randint(1, 3)
rocks = 0
rock_health = random.randint(1, 2)
heat = False


def action():
    global berries, bush_health, wood, stick_health, rocks, rock_health, wood, axe, zombie_health, collect_rad_away,\
        rad_aways, rad_away_health
    if player.distance(bush) < 50:
        berries += 1
        bush_health -= 1
    if player.distance(stick) < 40:
        wood += 1
        stick_health -= 1
    if player.distance(rock) < 20:
        rocks += 1
        rock_health -= 1
    if player.distance(tree) < 50 and axe is True:
        wood += 2
    if player.distance(zombie) < 40:
        zombie_health -= 1


berries = 0
food_left = 100


def eat():
    global food_left, berries
    if berries > 0:
        food_left += 10
        berries -= 1


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


health = 100
hydration = 100
warmth = 100
campfire_health = 0
game_time = 0
zombie_attack = False
start = time.time()
alive = True
test_time = 0


def tick_update():
    global food_left, berries, health, hydration, warmth, bush_health, stick_health, rock_health,\
        campfire_health, heat, game_time, zombie_attack, zombie_health, alive, rocks, wood, test_time
    food_left -= 1
    hydration -= 1
    game_time += 1
    test_time += 1
    fire.shape('images/campfire2.gif')

    if rocks <= 0:
        rocks = 0

    if wood <= 0:
        wood = 0

    if zombie_health <= 0:
        zombie_health = 7
        zombie.hideturtle()
        zombie.setpos(random.randint(-275, 275), random.randint(-275, 275))
        zombie.showturtle()

    if game_time >= 12:
        window.bgcolor('Dim Gray')
        warmth -= 1
        zombie_attack = True
        zombie.showturtle()
        if zombie.ycor() > player.ycor():
            zombie.setpos(zombie.xcor(), zombie.ycor() - 10)
            zombie.shape('images/zombie3.gif')

        if zombie.ycor() < player.ycor():
            zombie.setpos(zombie.xcor(), zombie.ycor() + 10)
            zombie.shape('images/zombie1.gif')

        if zombie.xcor() > player.xcor():
            zombie.setpos(zombie.xcor() - 10, zombie.ycor())
            zombie.shape('images/zombie4.gif')

        if zombie.xcor() < player.xcor():
            zombie.setpos(zombie.xcor() + 10, zombie.ycor())
            zombie.shape('images/zombie2.gif')
    else:
        zombie.hideturtle()
        zombie_attack = False

    if test_time < 4 and player.xcor() == 300 and player.ycor() == 300:
        test_object.shape('images/dont_copyright_strike_me_plz.gif')
        test_object.showturtle()
        print('50 72 6f 67 72 61 6d 69 6e 67 3a 20 42 61 73 69 '
              '6c 20 53 2e 20 48 65 6c 70 3a 20 41 6e 74 6f 6e '
              '20 53 2e 20 28 6c 6f 74 20 6f 66 20 68 65 6c 70 '
              '20 74 68 6f 29 20 47 72 61 70 68 69 63 73 3a 3f 21 3f 31')
        time.sleep(0.25)
        test_object.hideturtle()
        window.bye()

    if zombie_attack is True and zombie.distance(player) < 30:
        health -= 1

    if health > 100:
        health = 100

    if food_left >= 85 and hydration >= 85 and warmth >= 85:
        health += 1

    if game_time >= 24:
        game_time = 0
        window.bgcolor('Sea Green')

    if heat is True:
        campfire_health -= 1

    if campfire_health <= 0:
        heat = False
        campfire_health = 0
        fire.hideturtle()

    if food_left <= 0:
        health -= 10
        food_left = 0

    if health <= 0:
        wasted_screen.penup()
        wasted_screen.setpos(-110, 0)
        wasted_screen.color('red')
        end = time.time()
        final_time = (end - start) / 24
        wasted_screen.write("WASTED", font=("Arial", 45, "normal"))
        wasted_screen.setpos(-100, -35)
        wasted_screen.write("You Survived For: %s Days" % (int(final_time)), font=("Arial", 15, "normal"))
        alive = False
        health = 0

    turtle.undo()
    turtle.hideturtle()
    turtle.penup()
    turtle.setpos(-300, 270)
    turtle.write('food left: %s, berries: %s, health: %s, hydration: %s, warmth: %s, wood:'
                 ' %s, rocks: %s, campfire health: %s, time: %s' %
                 (food_left, berries,  health, hydration, warmth, wood, rocks,
                  campfire_health, game_time), font=("Arial", 9, "normal"))

    if food_left >= 100:
        food_left = 100

    if player.distance(water) < 50:
        hydration += 2
        warmth -= 1

    if hydration >= 100:
        hydration = 100

    if hydration <= 0:
        health -= 10
        hydration = 0

    if warmth <= 0:
        health -= 10
        warmth = 0

    if warmth >= 100:
        warmth = 100

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

    fire.shape('images/campfire1.gif')

    if alive is True:
        turtle.ontimer(tick_update, 350)


turtle.onkeypress(up, 'w')
turtle.onkeypress(down, 's')
turtle.onkeypress(left, 'a')
turtle.onkeypress(right, 'd')
turtle.onkeypress(action, 'e')
turtle.onkeypress(eat, '1')
turtle.onkeypress(build_campfire, '2')
turtle.onkeypress(craft_axe, '3')

tick_update()

turtle.listen()

turtle.mainloop()
