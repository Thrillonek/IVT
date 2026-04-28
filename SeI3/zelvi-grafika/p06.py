import turtle, asyncio

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
# turtle.tracer(0) # obrázek se objeví instantně

turtles = [t1, t2, t3]

size = 100
gap_multiplier = 1.5

def square(a, t): # funkce pro kresbu čtverce se stranou o délce a
  for _ in range(4):
    t.forward(a)
    t.right(90)

colors = ["blue", "green", "red"]

for t in turtles:
  t.penup()

t1.setx(size * gap_multiplier * -1)
t3.setx(size * gap_multiplier)

def draw_square(t):
  t.pendown()
  t.fillcolor(colors[turtles.index(t)])
  t.begin_fill()
  square(size, t)
  t.end_fill()

for idx, t in enumerate(turtles):
  draw_square(t)

turtle.done()