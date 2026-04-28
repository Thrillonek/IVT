import turtle, asyncio

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
# turtle.tracer(0) # obrázek se objeví instantně

turtles = [t1, t2, t3]
colors = ["blue", "green", "red"]

size = 100
gap_multiplier = 1.5

for t in turtles:
  t.penup()

t1.setx(size * gap_multiplier * -1)
t3.setx(size * gap_multiplier)

for idx, t in enumerate(turtles):
  t.pendown()
  t.speed(100)
  t.fillcolor(colors[idx])
  t.begin_fill()

for _ in range(4):
  for _ in range(10):
    for t in turtles:
      t.forward(size / 10)
  for t in turtles:
    t.left(90)

for idx, t in enumerate(turtles):
  t.end_fill()

turtle.done()