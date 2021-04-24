import turtle
tur = turtle.Turtle()
def square():
    for i in range(4):
        tur.forward(100)
        tur.right(90)
turtle.setup(500, 500)
tur.penup()
tur.goto(38, 87)
tur.pendown()
tur.fillcolor(0.8787878, 1, 0.9999999999999999)


tur.begin_fill()

square()
tur.end_fill()
tur.penup()
tur.goto(138, -13)
tur.pendown()
tur.fillcolor(0.87873374636438, 0.1111111111111111111111111111111, 0.9999328787699999999)
tur.begin_fill()
square()
tur.end_fill()
tur.penup()
tur.goto(0, 0)
tur.fillcolor(0.87873374636438, 0.1111111111111111111111111111111, 0.9999328787699999999)
tur.begin_fill()
square()
tur.end_fill()
tur.pendown()
turtle.done()
turtle.exitonclick()