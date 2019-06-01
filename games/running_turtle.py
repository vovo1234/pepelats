
import turtle

# Update period, milliseconds
tick_ms = 50

player = turtle.Turtle( )
player.shape( "triangle" )
player.color( "green" )

# Player speed
speed = 3

def update_world( ):
    global player
    global speed
    global tick_ms
    player.forward( speed )
    turtle.ontimer( update_world, tick_ms )

def faster( ):
    global speed
    speed = speed + 1

def slower( ):
    global speed
    speed = speed - 1

def left( ):
    global player
    player.left( 5 )

def right( ):
    global player
    player.right( 5 )

def toggle_draw( ):
    if player.isdown( ):
        player.penup( )
    else:
        player.pendown( )
    
turtle.onkeypress( left, 'Left' )
turtle.onkeypress( right, 'Right' )
turtle.onkeypress( faster, 'Up' )
turtle.onkeypress( slower, 'Down' )
turtle.onkeypress( toggle_draw, 'space' )
turtle.listen( )

update_world( )

turtle.listen( )
turtle.mainloop( )
