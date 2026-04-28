import turtle

t = turtle.Turtle()

t.pensize(1)
t.speed(5000)

t.penup()
t.setx(-150)
t.sety(-100)

t.pendown()

t.setheading(90)

count = 19

for i in range(count):
  t.forward((count-i)*10)
  t.right(90)

t.penup()
t.setx(300)
t.sety(100)
t.setheading(-45)

t.pendown()

for i in range(count*2):
  t.forward((count*2-i)*2)
  t.right(45)

turtle.done()