import turtle
text="Ulu Mosque \n (Bursa/Turkey)"
t=turtle.Turtle()
t.up(),t.goto(-200,-200)
t.pendown()
t.pensize(2)
turtle.bgcolor("light grey")
t.speed(100)
t.color("sandybrown")
t.begin_fill()
for i in range(2):
    t.fd(400)
    t.left(90)
    t.fd(200)
    t.left(90)
t.end_fill()
def tower():
    t.left(90)
    t.begin_fill()
    for i in range(2):
        t.fd(450)
        t.left(90)
        t.fd(50)
        t.left(90)
    t.end_fill()
    t.fd(450)
    t.left(90)
    t.color("brown")
    t.begin_fill()
    t.right(90)
    t.circle(25,180)
    t.end_fill()
    t.circle(25,-180)
    t.color("sandybrown")
    t.fd(-450)
    t.left(-90)
tower()
t.fd(450)
tower()
t.right(-90)
t.fd(200)
t.color("brown")
t.up()
t.circle(25,180)
t.right(180)
t.down()
t.begin_fill()
for i in range(5):
    t.circle(40,180)
    t.right(180)
t.end_fill()
t.up()
t.goto(-50,-200)
t.down()
t.color("black")
t.right(90)
t.begin_fill()
for i in range(2):
    t.fd(100)
    t.left(90)
    t.fd(150)
    t.left(90)
t.end_fill()
t.up()
t.backward(200)
t.down()
def windows():
    t.left(90)
    t.fd(100)
    t.right(180)
    t.circle(50,-180)
    t.right(180)
    t.fd(100)
    t.left(90)
windows(),windows()
t.up()
windows()
t.down()
windows(),windows()
t.up()
t.goto(300,300)
t.down()
t.write(text, align="left", font=("Arial", 20, "bold"))
t.up()
t.goto(8800,8888)
turtle.done()
###Ulu_Mosque###
