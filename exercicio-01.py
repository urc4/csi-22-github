import turtle
def draw_square(turtle_name,square_length):
    """Make turtle turtle_name draw a square of lenght square_length centered around the origin"""
    start_pos_x = -square_length/2;
    start_pos_y = -square_length/2;
    turtle_name.penup()
    turtle_name.setposition(start_pos_x,start_pos_y)
    turtle_name.pendown()
    turtle_name.pensize(3)
    turtle_name.pencolor("orange")
    for i in range(4):
        turtle_name.forward(square_length)
        turtle_name.left(90)

def draw_squares_inside_out(turtle_name,number_squares):
    step = 40
    sq_len = 80
    for i in range(number_squares):
        draw_square(turtle_name,sq_len)
        sq_len = sq_len + step

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Exercicio 1")
michelangelo = turtle.Turtle()
draw_squares_inside_out(michelangelo,5)
window.mainloop()