import turtle

t = turtle.Turtle()

t.pensize(1)
t.speed(500)

t.penup()
t.setx(-250)

t.pendown()

t.setheading(90)

count = 500

for i in range(count):
  t.forward((count-i)*0.03)
  t.right(4.5)

turtle.done()