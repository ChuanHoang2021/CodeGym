import turtle

t = turtle.Turtle()
t.pencolor('blue')
a = int(input("Nhập chiều rộng a=:"))
b = int(input("Nhập chiều dài b=:"))
def hcn(a,b):
    global x
    global y
    x = a
    y = b
    for i in range(2):
        t.begin_fill()
        t.fillcolor('red')
        t.forward(a)
        t.lt(90)
        t.forward(b)
        t.lt(90)
        t.end_fill()
    t.penup()
    t.fd(a/3)
    t.lt(90)
    t.fd(y/3)
    t.rt(90)
    t.pendown()
    for i in range(2):
        t.begin_fill()
        t.fillcolor('white')
        t.fd(a/3)
        t.lt(90)
        t.fd(b/3)
        t.lt(90)
        t.end_fill()
    t.penup()
    t.goto(0,0)
    t.pendown()

def nhakho(a):
    for i in range(4):
        t.begin_fill()
        t.fillcolor('red')
        t.fd(1.5 * a)
        t.lt(90)
        t.end_fill()
    t.penup()
    t.fd(1.5*a/4)
    t.pendown()
    t.begin_fill()
    t.fillcolor('green')
    t.lt(90)
    t.fd(b/2)
    t.rt(90)
    t.fd(1.5*a/2)
    t.rt(90)
    t.fd(b/2)
    t.rt(90)
    t.fd(1.5 * a / 2)
    t.end_fill()


hcn(a,b)

t.penup()
t.fd(a)
t.pendown()
hcn(a,b)

t.penup()
t.lt(90)
t.fd(b)
t.rt(90)
t.pendown()
hcn(a,b)

t.penup()
t.goto(a,b)
t.pendown()
hcn(a,b)

t.penup()
t.goto(2*a,0)
t.pendown()

nhakho(a)




turtle.done()