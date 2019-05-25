
import turtle

def draw_house_anya( x, y, size, house_color, roof_color, door_color ):
    # Move turtle to where we want to draw
    turtle.up( )
    turtle.setpos( x - size / 2.0, y )
    turtle.setheading( 0 )
    turtle.down( )

    # draw box
    turtle.color( house_color )
    turtle.begin_fill()
    for x in range(0,4):
        turtle.forward( 100 * size / 100.0 )
        turtle.left(90)
    turtle.end_fill()

    # move to the roof initial position
    for x in range(0,2):
        turtle.forward( 100 * size / 100.0 )
        turtle.left(90)

    # draw roof
    turtle.color( roof_color )
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward( 70.71067811865475 * size / 100.0 )
    turtle.left(90)
    turtle.forward( 70.71067811865475 * size / 100.0 )
    turtle.end_fill()

    # go to the door
    turtle.up( )
    turtle.left(45)
    turtle.forward(100 * size / 100.0)
    turtle.left(90)
    turtle.forward(33.333 * size / 100.0)
    turtle.down( )

    # draw door
    turtle.color( door_color )
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(65 * size / 100.0)
    turtle.right(90)
    turtle.forward(33.333 * size / 100.0)
    turtle.right(90)
    turtle.forward(65 * size / 100.0)
    turtle.end_fill()

def draw_house_lex( x, y, size, house_color, roof_color, door_color ):
    # Move turtle to where we want to draw
    turtle.up( )
    turtle.setpos( x - size / 2.0, y )
    turtle.setheading( 0 )
    turtle.down( )

    turtle.color( house_color )
    turtle.begin_fill( )
    for x in range (0,6):
        turtle.forward(100 * size / 100.0)
        turtle.left(90)
    turtle.end_fill( )

    turtle.color( roof_color )
    turtle.begin_fill( )
    turtle.right(45)
    turtle.forward(70 * size / 100.0)
    turtle.left(90)
    turtle.forward(71 * size / 100.0)
    turtle.end_fill( )
    turtle.up()
    turtle.left(45)
    turtle.forward(20 * size / 100.0)
    turtle.left(90)
    turtle.forward(20 * size / 100.0)
    turtle.down()

    turtle.color( roof_color, 'white' )
    turtle.begin_fill( )
    for x in range (0,4):
        turtle.forward(60 * size / 100.0)
        turtle.right(90)
        
    turtle.forward(30 * size / 100.0)
    turtle.right(90)
    turtle.forward(60 * size / 100.0)
    turtle.end_fill( )

def draw_house( x, y, size, type, house_color, roof_color, door_color ):
    if type == 'anya':
        draw_house_anya( x, y, size, house_color, roof_color, door_color )
    if type == 'lex':
        draw_house_lex( x, y, size, house_color, roof_color, door_color )

# Calculates on-screen scale from the world coordinates
def world_to_scale( x, y ):
    k = 0.05
    return (y + 100 ) * k
    
# World coordinates to screen. World visible area is approximatesly -50 to 50
# both x and y, y is pointed towards the camera
def world_to_screen( x, y ):
    scale = world_to_scale( x, y )
    x_screen = int( x * scale )
    y_screen = int( -50 * scale ) + 200
    return ( x_screen, y_screen )

def draw_field( ):
    # green field!
    turtle.up( )
    turtle.setpos( world_to_screen( -55, -55 ) )
    turtle.color( 'darkgreen' )
    turtle.begin_fill( )
    turtle.setpos( world_to_screen( -55,  55 ) )
    turtle.setpos( world_to_screen(  55,  55 ) )
    turtle.setpos( world_to_screen(  55, -55 ) )
    turtle.setpos( world_to_screen( -55, -55 ) )
    turtle.end_fill( )

