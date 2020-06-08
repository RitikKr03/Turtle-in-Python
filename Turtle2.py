import turtle
import random
x=turtle.Turtle()
colors=['red','blue','green','purple','yellow','orange','black']

x.color('red','blue')
x.width(5)

x.begin_fill()
x.circle(50)
x.end_fill()

x.penup()
x.forward(150)
x.pendown()
x.color('yellow','black')

x.begin_fill()
for y in range(4):
    x.forward(100)
    x.right(90)
x.end_fill()

for y in range(5):
    randColor=random.randrange(0,len(colors))
    x.color(colors[randColor],colors[random.randrange(0,len(colors))])
    rand1=random.randrange(-300,300)
    rand2=random.randrange(-300,300)
    x.penup()
    x.setpos((rand1,rand2))
    x.pendown()
    x.begin_fill()
    x.circle((random.randrange(0,80)))
    x.end_fill()