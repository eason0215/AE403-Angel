import turtle
tur = turtle.Turtle()
def rectangle():
    tur.begin_fill()
    tur.forward(800)
    tur.right(90)
    tur.forward(200)
    tur.right(90)
    tur.forward(800)
    tur.right(90)
    tur.forward(200)
    tur.right(90)
    tur.end_fill()
def myGoto(x, y):
    tur.penup()
    tur.goto(x, y)
    tur.pendown()

turtle.setup(850, 650, 0, 0)

myGoto(-400, 300)
tur.fillcolor(0, 0, 0)

rectangle()


myGoto(-400, 100)
tur.fillcolor(1, 0, 0)

rectangle()

myGoto(-400, -100)
tur.fillcolor(1, 1, 0)

rectangle()


turtle.done()
turtle.exitonclick()

        