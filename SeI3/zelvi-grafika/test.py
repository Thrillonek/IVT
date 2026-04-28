from turtle import *
 
tracer(0)

penup()
sety(150)
pendown()
 
a, b, n = 100, 50, 100
 
# květ
for _ in range(18):
    for _ in range(4):
        forward(b)
        left(90)
    left(20)
 
# stonek
right(90)
forward(100)
left(70)
 
for i in range(2, 14):
    s = (-1)**i
    for _ in range(25):
        left(s * (360/n))   # oprava tady
        forward(a/n + i*a/(3*n))
    left(s * 90)
    for _ in range(25):
        left(s * (360/n))   # oprava tady
        forward(a/n + i*a/(3*n))
    left(s * 20)
    forward(27)
    right(s * 70)
 
exitonclick()