import turtle

t = turtle.Turtle()

floor_height = 25
floor_count = 10
floor_length_k = 2

t.pensize(1)
t.speed(500)

t.penup()

t.setx(-250)
t.sety(-100)

t.pendown()

def rectangle(a):
  for _ in range(2):
    t.forward(a)
    t.right(90)
    t.forward(floor_height)
    t.right(90)

for i in range(floor_count):
  calculateLength = lambda a: (floor_count - a) * 2

  rectangle(calculateLength(i) * floor_height)
  t.penup()
  t.forward((calculateLength(i) - calculateLength(i + 1)) * floor_height / 2)
  t.left(90)
  t.forward(floor_height)
  t.right(90)
  t.pendown()

turtle.done()