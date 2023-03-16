import turtle
import math
def draw_poly(t,n,sz):
    """Make turtle turtle_name draw a polygon of n sides each with lenght sz from the origin"""
    pos_x = 0;
    pos_y = 0;
    angle_step = 2*math.pi/n
    ang = 0
    t.pensize(3)
    t.pencolor("orange")
    for i in range(n):
      ang = ang + angle_step
      pos_x = pos_x + math.cos(ang)*sz
      pos_y = pos_y + math.sin(ang)*sz
      t.goto(pos_x,pos_y)
      # could do this by using left



window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Exercicio 2")
donatello = turtle.Turtle()
draw_poly(donatello,7,100)
window.mainloop()