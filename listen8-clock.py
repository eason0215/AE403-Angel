import turtle
import time 
import datetime

tur = turtle.Turtle()
tur.seth(90)
tur.speed(10)
turtle.setup(800, 800)
def writeNumber(num):
    tur.penup()
    tur.forward(200)
    tur.write(num)
    tur.back(200)
for i in range(1, 13):
    tur.right(30)
    writeNumber(i)
    
tur.forward(230)
tur.left(90)
tur.pendown()
tur.circle(230)
tur.hideturtle()
update = True
updateSecond = True
while True:
    now = datetime.datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second
   

    if update:
        #h
        hour = turtle.Turtle()
        hour.seth(90)
        hour.right((h + m / 60) * 30)
        hour.pensize(3)
        hour.color(1, 0, 0)
        hour.hideturtle()
        hour.forward(100)
    
        #m
        minute = turtle.Turtle()
        minute.seth(90)
        minute.right(m * 6)
        minute.pensize(3)
        minute.color(0, 0, 1)
        minute.hideturtle()
        minute.forward(150)
        update = False
    if updateSecond:
        second = turtle.Turtle()
        second.seth(90)
        second.right(s * 6)
        second.pensize(1)
        second.color(0, 0, 0)
        second.hideturtle()
        second.forward(180)
        updateSecond = False
    time.sleep(1)
    now = datetime.datetime.now()
    mNew = now.minute
    sNew = now.second
    if mNew != m:
        update = True
        hour.clear()
        hour.reset()
        minute.clear()  
        minute.reset()
    if sNew != s:
        updateSecond = True
        second.clear()
        second.reset()
       
turtle.done()
turtle.exitonclick()
    