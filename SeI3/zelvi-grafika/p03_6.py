import turtle

t = turtle.Turtle()

t.pensize(1)
t.speed(500)

t.penup()

t.pendown()

def square(a):
  for _ in range(4):
    t.forward(a)
    t.right(90)

t.setheading(90)

for _ in range(18):
  square(100)
  t.right(20)

turtle.done()