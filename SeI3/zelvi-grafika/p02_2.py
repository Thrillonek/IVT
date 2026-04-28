import turtle
import math

t = turtle.Turtle()

t.pensize(2)
t.penup()
t.speed(500)

t.setx(-400)
t.pendown()

for count in range(5, 9):
  angle = ((count - 2) / count) * 180
  for _ in range(count):
    t.forward(300/count)
    t.right(180 - angle)

  t.penup()
  t.setheading(0)
  t.forward(200)
  t.pendown()

turtle.done()