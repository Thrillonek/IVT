import turtle

t = turtle.Turtle()

t.pensize(5)
t.penup()

t.setx(-125)
t.sety(-125)

t.pendown()

for _ in range(3):
  t.forward(250)
  t.left(120)

turtle.done()
