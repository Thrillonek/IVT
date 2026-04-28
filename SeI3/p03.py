import time

def scitani(cislo1, cislo2):
  return cislo1 + cislo2

def odcitani(cislo1, cislo2):
  return cislo1 - cislo2

def nasobeni(cislo1, cislo2):
  return cislo1 * cislo2

def deleni(cislo1, cislo2):
  return cislo1 / cislo2

cislo1 = int(input("Číslo jedna: "))
cislo2 = int(input("Číslo dva: "))
operace = input("Operace: ")

print("Přemýšlím...")
time.sleep(5)
print("Furt přemýšlím...")
time.sleep(5)

if operace == "+":
  print(scitani(cislo1, cislo2))
elif operace == "-":
  print(odcitani(cislo1, cislo2))
elif operace == "*":
  print(nasobeni(cislo1, cislo2))
elif operace == "/":
  print(deleni(cislo1, cislo2))
