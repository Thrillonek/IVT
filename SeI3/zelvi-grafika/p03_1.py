import turtle

t = turtle.Turtle()

t.pensize(1)
t.speed(5000)

t.penup()

t.right(180)

for _ in range(2):
  t.forward(50)
  t.right(90)

t.pendown()

count = int(input("Zadej číslo: "))
angle = ((count - 2) / count) * 180

for _ in range(count):
  t.forward(300/count)
  t.right(180 - angle)

turtle.done()