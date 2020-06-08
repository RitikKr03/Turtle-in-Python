import turtle
import random

x = turtle.Turtle()
x.speed(0)
x.width(5)
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']


def up():
    x.setheading(90)
    x.forward(100)


def down():
    x.setheading(270)
    x.forward(100)


def left():
    x.setheading(180)
    x.forward(100)


def right():
    x.setheading(0)
    x.forward(100)


def clickLeft(x, y):
    x.color(random.choice(colors))


def clickRight(x, y):
    x.stamp()


x.listen()

turtle.onscreenclick(clickLeft, 1)
turtle.onscreenclick(clickRight, 3)

x.onkey(up, 'Up')
x.onkey(down, 'Down')
x.onkey(left, 'Left')
x.onkey(right, 'Right')

x.mainloop()
