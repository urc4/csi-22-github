import turtle


def draw_poly(t, n, sz):
    """Make turtle turtle t draw a polygon of n sides 
    each with lenght sz starting from the origin"""
    ang_step = 360/n

    t.pensize(3)
    t.pencolor("orange")

    for i in range(n):
        t.forward(sz)
        t.left(ang_step)


window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Exercicio 2")
donatello = turtle.Turtle()
draw_poly(donatello, 8, 50)
window.mainloop()
