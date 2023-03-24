import turtle


def draw_spiral(t, turn_ang, num_spirals):
    """Make turtle t draw num_spirals of base size sz incremented every step
    by rotating it by a step angle turn_ang"""
    t.pensize(3)
    t.pencolor("blue")

    sz = 5
    step = 5

    t.right(90)

    for i in range(num_spirals*4 - 1):
        t.forward(sz)
        t.right(turn_ang)
        sz = sz + step


wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Exercicio 4")
leonardo = turtle.Turtle()
turn_ang = 90
turn_ang = 88.8
num_spirals = 20
draw_spiral(leonardo, turn_ang, num_spirals)

wn.mainloop()
