"""
Spočítej obsah pozemku, když nám uživatel zadá šířku a délku.
Dej uživateli možnost zadat lokalitu pozemku a to tak, že při výběru lokality
se zohlední i cena za metr čtvereční platná pro tuto lokalitu.
Pak vypočítej cenu.
"""

praha = 2000
brno = 10
ostrava = 500
havirov = 1000

def intInput(text):
    return int(input(text))

def newLine(number):
    for i in range(number):
        print("")

width = intInput('Zadej šířku tvého pozemku: ')
length = intInput('Zadej délku tvého pozemku: ')

newLine(1)

print("Zadej číslo lokality pozemku:")
print("Praha - 1")
print("Brno - 2")
print("Ostrava - 3")
print("Havířov - 4")

newLine(1)

location = int(input())

area = width * length
areaAr = area / 100

def calcPrice(location):
    price = area * location
    print("Pozemek stojí", price, "korun.")

if location == 1:
    calcPrice(praha)
if location == 2:
    calcPrice(brno)
if location == 3:
    calcPrice(ostrava)
if location == 4:
    calcPrice(havirov)
else:
    print("Špatná hodnota lokace.")

newLine(1)

print("Obsah pozemku je", areaAr, "arů.", end="\n\n")
