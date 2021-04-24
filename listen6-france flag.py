import turtle
tur = turtle.Turtle()
def rectangle():
    tur.begin_fill()
    tur.forward(250)
    tur.right(90)
    tur.forward(600)
    tur.right(90)
    tur.forward(250)
    tur.right(90)
    tur.forward(600)
    tur.right(90)
    tur.end_fill()
def myGoto(x, y):
    tur.penup()
    tur.goto(x, y)
    tur.pendown()

turtle.setup(850, 650, 0, 0)

myGoto(-400, 300)
tur.fillcolor(0, 0, 1)

rectangle()


myGoto(-150, 300)
tur.fillcolor(1, 1, 1)

rectangle()

myGoto(100, 300)
tur.fillcolor(1, 0, 0)

rectangle()


turtle.done()
turtle.exitonclick()

