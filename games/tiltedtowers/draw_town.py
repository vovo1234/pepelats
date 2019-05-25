
import turtle
import random
import town
from town import *

turtle.speed( 'fastest' )
turtle.tracer( False )

draw_field( )

num_of_rows = 14
num_of_cols = 14

for r in range( 0, num_of_rows ):
    for c in range( 0, num_of_cols ):
        x = ( c - (num_of_cols - 1) / 2 ) * 7 + random.uniform( -1.0, 1.0 )
        y = ( r - (num_of_rows - 1) / 2 ) * 7
        x_screen, y_screen = world_to_screen( x, y )
        size = 3 * world_to_scale( x, y )
        type_list = [ 'lex', 'anya' ]
        house_type = random.choice( type_list )
        color_list = [ 'yellow', 'orange', 'red', 'maroon', 'violet',
                       'magenta', 'navy', 'blue', 'cyan', 'turquoise',
                       'chocolate', 'gray' ]
        house_color = random.choice( color_list )
        color_list.remove( house_color )
        roof_color = random.choice( color_list )
        color_list.remove( roof_color )
        door_color = random.choice( color_list )
        color_list.remove( door_color )
        draw_house( x_screen, y_screen, size, house_type,
                    house_color, roof_color, door_color )
