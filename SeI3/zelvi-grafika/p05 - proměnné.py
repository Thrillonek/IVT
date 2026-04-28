import turtle

t = turtle.Turtle()
turtle.tracer(0) # obrázek se objeví instantní

blossom_size = 100 # velikost květu
blossom_color = "purple" # barva květu
blossom_center_color = "yellow" # barva středu květu
blossom_center_ratio = 0.5 # poměr středu květu a květu samotného 
blossom_count = 14 # počet okvětních lístků
leaf_gap = 30 # mezera mezi listy (svisle)
leaf_size = 1 # velikost listu
leaf_multiplier = 1/20 # jak rychle se zvětšují listy
leaf_radius = 60 # jak široké jsou listy
leaf_angle = 0 # jak moc nakloněné jsou listy

t.penup()

t.sety(200)
t.setx(0)

t.pendown()

def square(a): # funkce pro kresbu čtverce se stranou o délce a
  for _ in range(4):
    t.forward(a)
    t.right(90)

# vykreslí začátek stonku
t.setheading(270)
t.color("green")
t.pensize(3)
t.forward(blossom_size + leaf_gap * 2)

# funkce pro vykreslení listu
# a = velikost
# side = strana zatáčení
def leaf(a, side): 
  def turn(angle, side):
    if side == "left":
      t.left(angle)
    elif side == "right":
      t.right(angle)

  t.pensize(1)
  t.fillcolor("green")
  t.begin_fill()

  for i in range(2):
    for _ in range(12):
      t.forward(a / 6)
      turn(leaf_radius / 12, side)
    if i == 0:
      turn(180 - leaf_radius, side)

  t.end_fill()
  t.pensize(3)

# vykreslí část stonku s listy
for i in range(12):
  side = "left"
  if i % 2 == 1:
    side = "right"
  
  t.forward(leaf_gap)
  t.setheading(180 * (i % 2) - leaf_angle * (1 - (i % 2) * 2))
  leaf((i * leaf_multiplier + leaf_size * 0.75) * leaf_gap * 2.25, side)
  t.setheading(270)

t.forward(leaf_gap)

# skočí na začátek (vrch stonku)
t.sety(200)

# vykreslí květ
t.setheading(315)
t.setx(0)
t.color(blossom_color)

for i in range(blossom_count):
  t.begin_fill()
  t.fillcolor(blossom_color)

  square(blossom_size)
  t.end_fill()
  t.right(360 / blossom_count)

# vykreslí střed květu
t.setheading(90)
t.setx(blossom_size * blossom_center_ratio)

t.color(blossom_center_color)
t.fillcolor(blossom_center_color)
t.begin_fill()
t.circle(blossom_size * blossom_center_ratio)
t.end_fill()

turtle.done()