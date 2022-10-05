import turtle
t = turtle.Turtle()

t.penup()
t.goto(-120,170)
t.pendown()
t.color("red")
t.begin_fill()
for i in range(2):
    t.forward(240)
    t.right(90)
    t.forward(340)
    t.right(90)
t.end_fill()


t.penup()
t.goto(-100,150)
t.pendown()
t.pencolor("white")
t.pensize(5)
for i in range(2):
    t.forward(200)
    t.right(90)
    t.forward(300)
    t.right(90)


t.penup()
t.goto(0,-50)
t.pendown()
t.circle(80)

t.penup()
t.goto(-28,-25)
t.pendown()
t.color("white")
t.begin_fill()
t.forward(30)
t.left(80)
t.forward(75)
t.right(80)
t.forward(30)
t.left(80)
t.forward(25)
t.left(100)
t.forward(90)
t.left(80)
t.forward(25)
t.left(100)
t.forward(30)
t.right(100)
t.forward(75)
t.end_fill()


t.penup()
t.goto(-70,-120)
t.pendown()
t.pencolor("white")
t.write("SERIES", font=("Arial", 20, "normal"))

t.hideturtle()
turtle.done()