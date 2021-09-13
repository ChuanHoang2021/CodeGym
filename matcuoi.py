import random
import turtle

#Khai báo biến
sc = turtle.Screen()
sc.bgcolor("pink")
pen = turtle.Turtle()
pen.pensize(5)
facesize = 200
maumat = ["red", "blue", "orange", "black"]
matsize = 18
pen.pencolor("yellow")
#Vẽ hình tròn khuôn mặt
pen.penup()
pen.goto(0,-facesize)
pen.pendown()
pen.fillcolor(random.choice(maumat))
pen.begin_fill()
pen.circle(facesize)
pen.end_fill()
#Vẽ mắt trái
pen.penup()
pen.goto(-100,50)
pen.pendown()
pen.fillcolor(random.choice(maumat))
pen.begin_fill()
pen.circle(matsize)
pen.end_fill()
#Vẽ mắt phải
pen.penup()
pen.goto(100,50)
pen.pendown()
pen.fillcolor(random.choice(maumat))
pen.begin_fill()
pen.circle(matsize)
pen.end_fill()
#Vẽ mũi tam giác
pen.penup()
pen.goto(0,50)
pen.pendown()
pen.fillcolor(random.choice(maumat))
pen.begin_fill()
pen.circle(-50, steps = 3)
pen.end_fill()
#Vẽ miệng
pen.penup()
pen.goto(-100,-25)
pen.pendown()
pen.rt(90)
pen.circle(100,180)



sc.mainloop()