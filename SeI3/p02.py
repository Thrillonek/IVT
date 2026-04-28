"""
Naprogramuj hru kámen nůžky papír.
"""
import random

knp = ["kámen", "nůžky", "papír"]

def printLine():
    print("")
    for _ in range(20):
        print("-", end="")
    print("")
    print("")

pokracovat = "Ano"

while pokracovat == "Ano":
    uzivatel = input("Zadej kámen, nůžky nebo papír: ")

    if not uzivatel in knp:
        print("\nZadal jsi nevhodné slovo.")
        printLine()
        continue

    ai = random.randrange(3)
    uIndex = knp.index(uzivatel)

    printLine()

    print("Počítač si vybral", knp[ai]+".")

    print("")

    if ai == uIndex:
        print("Je to remíza.")
    elif ai - uIndex in [1, -2]:
        print("Vyhrál jsi.")
    else:
        print("Prohrál jsi.")
    
    print("")

    if input("Chceš pokračovat v této hře? Pokud ne, napiš \"ne\", jinak napiš něco jiného: ") == "ne":
        pokracovat = "Ne"
        print("")
        print("Konec hry.")
        printLine()
    else:
        printLine()

exit()
