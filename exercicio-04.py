import turtle

def draw_spiral(_turtle,step_angle,number_spirals):
    """Make turtle _turtle draw a spiral of length by rotating it by a step angle"""    
    length = 5
    for i in range(number_spirals*4):
        _turtle.forward(length)
        _turtle.left(step_angle)
        length = length + 5
    

wn = turtle.Screen();
wn.bgcolor("lightgreen")
wn.title("_turtle meets a function")
leonardo= turtle.Turtle()
leonardo.pensize(3)
leonardo.pencolor("blue")
step_angle = 90
step_angle = 91
number_spirals = 100
draw_spiral(leonardo,step_angle,number_spirals)

wn.mainloop()

# 