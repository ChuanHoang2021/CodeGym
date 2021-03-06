import turtle
import math

pen = turtle.Turtle()
sc = turtle.Screen()
pen.pensize(3)
pen.color('#0099CC')
#1.Biến xác định kích thước từng đối tượng ez :))
mautuongnha = '#FFFF00'
maucuanha = '#550000'
maumainha = 'red'
mauthancay = '#666666'

#1.1 Kích thước ngôi nhà
chieudai = 300
chieucao = 100
#1.2 Kích thước cửa nhà
cuacao = chieucao*3/4
cuarong =chieudai/3
#1.3 Kích thước mái nhà
mainha = chieudai/2
h = mainha * math.sqrt(3) / 2
#1.4 Kích thước cây
lacay = mainha/4
htree = lacay * math.sqrt(3) / 2
htree2 = htree*1.5
lacay2 = lacay*1.5
xtree = -chieudai
ytree = chieucao*2
xtree2 = chieudai*1.1
ytree2 = chieucao*1.8


#Vinahouse
pen.fillcolor(mautuongnha)
pen.begin_fill()
pen.penup()
pen.backward(150)
pen.pendown()
pen.fd(chieudai)
pen.lt(90)
pen.fd(chieucao)
pen.lt(90)
pen.fd(chieudai)
pen.lt(90)
pen.fd(chieucao)
pen.end_fill()
pen.lt(90)
#door
pen.fillcolor(maucuanha)
pen.begin_fill()
pen.penup()
pen.goto(0,0)
pen.backward(50)
pen.pendown()
pen.lt(90)
pen.fd(cuacao)
pen.rt(90)
pen.fd(cuarong)
pen.rt(90)
pen.fd(cuacao)
pen.rt(90)
pen.fd(cuarong)
pen.end_fill()
#roof
pen.penup()
pen.goto(0,0)
pen.fd(chieudai/2)
pen.rt(90)
pen.fd(chieucao)
pen.rt(90)
pen.pendown()
pen.fillcolor(maumainha)
pen.begin_fill()
pen.lt(60)
pen.fd(mainha)
pen.rt(120)
pen.fd(mainha)
pen.rt(120)
pen.fd(mainha)
pen.end_fill()
#chimney
pen.penup()
pen.backward(mainha*3/4)
pen.rt(90)
pen.fd(h/2)
pen.pendown()
pen.fd(h/2)
pen.penup()
pen.fd(h/6)
pen.pendown()
pen.fd(h/2)
pen.lt(90)
pen.penup()
pen.fd(h/6)
pen.lt(90)
pen.penup()
pen.fd(h/6)
pen.pendown()
pen.fd(h/4)
pen.penup()
pen.fd(h/4)
pen.pendown()
pen.fd(h/6)
pen.penup()
pen.backward(h/6)
pen.lt(90)
pen.pendown()
pen.fd(h/6)
pen.penup()
pen.goto(0,0)

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
pen.fillcolor(mauthancay)
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
pen.rt(180)

#Right tree
#1
pen.penup()
pen.goto(xtree2,ytree2)
pen.backward(lacay2/2)
pen.lt(60)
pen.pendown()
pen.fillcolor('#CCFF00')
pen.begin_fill()
pen.fd(lacay2)
pen.rt(120)
pen.fd(lacay2)
pen.rt(120)
pen.fd(lacay2)
pen.rt(180)
pen.end_fill()
pen.penup()
pen.goto(xtree2,ytree2)
#2
pen.lt(90)
pen.backward(htree2*2)
pen.rt(90)
pen.backward(lacay2*2/2)
pen.lt(60)
pen.pendown()
pen.fillcolor('#33CC00')
pen.begin_fill()
pen.fd(lacay2*2)
pen.rt(120)
pen.fd(lacay2*2)
pen.rt(120)
pen.fd(lacay2*2)
pen.rt(180)
pen.end_fill()
pen.penup()
pen.goto(xtree2,ytree2)
#3
pen.lt(90)
pen.backward(htree2*5)
pen.rt(90)
pen.backward(lacay2*3/2)
pen.lt(60)
pen.pendown()
pen.fillcolor('#009966')
pen.begin_fill()
pen.fd(lacay2*3)
pen.rt(120)
pen.fd(lacay2*3)
pen.rt(120)
pen.fd(lacay2*3)
pen.rt(180)
pen.end_fill()
pen.penup()
pen.goto(xtree2,ytree2)
#4
pen.lt(90)
pen.backward(htree2*5)
pen.rt(90)
pen.backward(lacay2/2)
pen.lt(90)
pen.pendown()
pen.fillcolor(mauthancay)
pen.begin_fill()
pen.backward(htree*5)
pen.rt(90)
pen.fd(lacay2)
pen.lt(90)
pen.fd(htree*5)
pen.lt(90)
pen.fd(lacay2)
pen.end_fill()
pen.penup()
pen.goto(xtree2,ytree2)
pen.rt(180)


sc.mainloop()

