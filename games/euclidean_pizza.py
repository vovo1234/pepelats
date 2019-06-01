
import turtle

turtle.tracer( False )

num_of_slices = 20
num_of_rect = 7        # Pieces moved to rectangular

radius = 100

# Center of the reound pizza
round_x = -120
round_y =  100

# Corner of the rectangular pizza
rect_x = -200
rect_y = -100

# Status text position
text_x = 100
text_y = 100

# Draws the round pizza
def draw_round( ):
    global round_x, round_y, radius
    global num_of_slices, num_of_rect
    num_of_round = num_of_slices - num_of_rect
    turtle.color( 'black', 'yellow' )
    extent = 360.0 * num_of_round / num_of_slices
    turtle.up( )
    turtle.setpos( round_x, round_y )
    turtle.down( )
    turtle.begin_fill( )
    turtle.setheading( 90 )
    turtle.forward( radius )
    turtle.left( 90 )
    turtle.circle( radius, extent )
    turtle.left( 90 )
    turtle.forward( radius )
    turtle.end_fill( )
    turtle.up( )

# Draws rectangular pizza
def draw_rectangular( ):
    global rect_x, rect_y, radius
    global num_of_slices, num_of_rect
    slice_angle = 360.0 / num_of_slices
    turtle.up( )
    turtle.color( 'black', 'yellow' )
    turtle.setpos( rect_x, rect_y )
    turtle.setheading( 270 - slice_angle / 2 )
    turtle.down( )
    if num_of_rect:
        turtle.forward( radius )
    for i in range( num_of_rect ):
        turtle.begin_fill( )
        if i % 2:
            turn_direction = -1.0
        else:
            turn_direction = 1.0
        turtle.left( turn_direction * 90 )
        turtle.circle( turn_direction * radius, slice_angle )
        turtle.left( turn_direction * 90 )
        turtle.forward( radius )
        turtle.end_fill( )
    turtle.up( )

def draw_text( ):
    global text_x, text_y
    global num_of_slices, num_of_rect
    num_of_round = num_of_slices - num_of_rect
    turtle.up( )
    turtle.color( 'black' )
    turtle.setpos( text_x, text_y )
    turtle.write( f"slices : {num_of_slices}\n"
                  f"round : {num_of_round}\n"
                  f"rectangular : {num_of_rect}\n"
                  "(c)ut (u)ncut\n"
                  "change (n)umber\n"
                  "(r)round\n" )
    
def draw( ):
    turtle.clear( )
    draw_round( )
    draw_rectangular( )
    draw_text( )
    turtle.hideturtle( )
    turtle.update( )

def cut( ):
    global num_of_slices, num_of_rect
    if num_of_rect < num_of_slices:
        num_of_rect = num_of_rect + 1
        draw( )

def uncut( ):
    global num_of_slices, num_of_rect
    if num_of_rect > 0:
        num_of_rect = num_of_rect - 1
        draw( )

def reset( ):
    global num_of_rect
    num_of_rect = 0
    draw( )

def change_number( ):
    global num_of_slices, num_of_rect
    num_of_slices = int( turtle.numinput( "Pizza", "Number of slices:",
                                     minval = 1 ) )
    if num_of_rect > num_of_slices:
        num_of_rect = num_of_slices
    turtle.listen( )
    draw( )
    
draw( )

turtle.onkeypress( cut, 'Up' )
turtle.onkeypress( cut, 'c' )
turtle.onkeypress( uncut, 'Down' )
turtle.onkeypress( uncut, 'u' )
turtle.onkeypress( reset, 'r' )
turtle.onkeypress( change_number, 'n' )

turtle.listen( )
turtle.mainloop( )
