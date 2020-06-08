import turtle
from turtle import Screen, Turtle

screen = Screen()
t = Turtle("turtle")
t.speed(-1)


def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)


def clickright(x,y):
    t.clear()


def main():
    turtle.listen()
    t.color('red')
    t.ondrag(dragging)
    turtle.onscreenclick(clickright,3)

    screen.mainloop()

main()


