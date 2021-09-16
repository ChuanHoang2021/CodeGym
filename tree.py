import turtle
import math

pen = turtle.Turtle()
sc = turtle.Screen()
pen.pensize(3)
pen.color('#0099CC')
#Biến
mautuongnha = '#FFFF00'
maucuanha = '#550000'
maumainha ='red'

chieudai = 300
chieucao = 100

cuacao = chieucao*3/4
cuarong =chieudai/3

mainha = chieudai/2
h = mainha * math.sqrt(3) / 2

lacay = mainha/4
htree = lacay * math.sqrt(3) / 2

xtree = 0
ytree = 0



#Left tree
#1
pen.penup()
pen.goto(xtree,ytree)
pen.backward(lacay/2)
pen.lt(60)
pen.pendown()
pen.fillcolor('#CCFF00')
pen.begin_fill()
pen.fd(lacay)
pen.rt(120)
pen.fd(lacay)
pen.rt(120)
pen.fd(lacay)
pen.rt(180)
pen.end_fill()
pen.penup()
pen.goto(xtree,ytree)
#2
pen.lt(90)
pen.backward(htree*2)
pen.rt(90)
pen.backward(lacay*2/2)
pen.lt(60)
pen.pendown()
pen.fillcolor('#33CC00')
pen.begin_fill()
pen.fd(lacay*2)
pen.rt(120)
pen.fd(lacay*2)
pen.rt(120)
pen.fd(lacay*2)
pen.rt(180)
pen.end_fill()
pen.penup()
pen.goto(xtree,ytree)
#3
pen.lt(90)
pen.backward(htree*5)
pen.rt(90)
pen.backward(lacay*3/2)
pen.lt(60)
pen.pendown()
pen.fillcolor('#009966')
pen.begin_fill()
pen.fd(lacay*3)
pen.rt(120)
pen.fd(lacay*3)
pen.rt(120)
pen.fd(lacay*3)
pen.rt(180)
pen.end_fill()
pen.penup()
pen.goto(xtree,ytree)
#4
pen.lt(90)
pen.backward(htree*5)
pen.rt(90)
pen.backward(lacay/2)
pen.lt(90)
pen.pendown()
pen.fillcolor('#666666')
pen.begin_fill()
pen.backward(htree*5)
pen.rt(90)
pen.fd(lacay)
pen.lt(90)
pen.fd(htree*5)
pen.lt(90)
pen.fd(lacay)
pen.end_fill()
pen.penup()
pen.goto(xtree,ytree)


sc.mainloop()