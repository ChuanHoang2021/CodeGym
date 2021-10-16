import random
import turtle

x,y = 100, 100
sc=turtle.Screen()
t = turtle.Turtle()
turtle.bgcolor("black")
n=0
c=0
while n<40:
    n+=1
    c+=1
    t.pencolor(random.choice(['blue','red', 'yellow', 'green']))
    t.penup()
    t.goto(-x,-y)
    t.pendown()
    t.rt(c)
    t.circle(70)

sc.mainloop()