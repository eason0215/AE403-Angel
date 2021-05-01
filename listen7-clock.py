import turtle

tur = turtle.Turtle()
tur.seth(60)
def writeNumber(num):
    tur.penup()
    tur.forward(200)
    tur.write(num)
    tur.back(200)
for i in range(1, 13):
    writeNumber(i)
    tur.right(30)


turtle.done()
turtle.exitonclick()
    
    

