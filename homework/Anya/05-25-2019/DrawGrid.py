import turtle
turtle.speed (100000)
 
def draw_grid(x_size, y_size, x_step, y_step):
    x_width = x_step*x_size
    x_min = -x_width/2
    x_max = x_width/2
    
    y_width = y_step*y_size
    y_min = -y_width/2
    y_max = y_width/2
    
    y_level = y_min
    for i in range (y_size+1):
        turtle.penup ()
        turtle.setpos (x_min, y_level)
        turtle.pendown ()
        turtle.setpos (x_max, y_level)
        y_level = y_level + y_step

    x_level = x_min
    for i in range (x_size+1):
        turtle.penup ()
        turtle.setpos (x_level, y_min)
        turtle.pendown ()
        turtle.setpos (x_level, y_max)
        x_level = x_level + x_step


draw_grid (10,1,600,100)
