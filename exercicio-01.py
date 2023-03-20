import turtle
def draw_square(t,sz):
    """Make turtle t draw a square of szght sz 
    centered around the origin"""
    start_pos_x = -sz/2;
    start_pos_y = -sz/2;
    t.penup()
    t.setposition(start_pos_x,start_pos_y)
    
    t.pensize(3)
    t.pencolor("orange")
    t.pendown()

    for i in range(4):
        t.forward(sz)
        t.left(90)

def draw_squares_inside_out(t,num_squares):
    """ Turtle t draws concentric num_squares squares 
    from inside out using the draw_square function"""
    step = 20
    sq_sz = 20

    for i in range(num_squares):
        draw_square(t,sq_sz)
        sq_sz = sq_sz + step



window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Exercicio 1")
michelangelo = turtle.Turtle()
draw_squares_inside_out(michelangelo,5)
window.mainloop()