import turtle

t = turtle.Turtle()

t.pensize(1)
t.speed(5000)

t.penup()

t.sety(100)

t.pendown()

for _ in range(95):
  t.forward(5)
  t.right(360 / 95)

turtle.done()