import turtle
import math

t = turtle.Turtle()

t.pensize(2)
t.penup()
t.speed(500)

t.setx(-400)

t.pendown()

length = 50

def turn(angle):
  t.left(angle)
def go(diagonal = False, multiplier = 1):
  distance = length * multiplier
  if diagonal:
    distance = math.sqrt(2) * distance
  t.forward(distance)

for _ in range(10):
  go()
  turn(90)
  go()
  turn(45)
  go(True, 1/2)
  turn(90)
  go(True, 1/2)
  turn(135)
  go()
  turn(225)
  go(True)
  turn(225)
  go()
  turn(225)
  go(True)
  turn(45)
  t.color("lime")
  go(False, 1/4)
  t.color("black")


turtle.done()