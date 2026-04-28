from random import choice

rps = ["kámen", "nůžky", "papír"]

while True:
    ai_bot = choice(rps) #Tah počítače
    clovek = input("Napiš, co chceš zahrát (kámen, nůžky, papír): ") #Tah hráče

    #Zkontroluje, zda hráč zadal platnou možnost
    if clovek not in rps:
        print("Tvoje odpověď není platná (zkontroluj, že jsi napsal háčky a čárky).")
    else:
        print("Počítač si vybral "+ai_bot+".") #Vypíše, co si vybral počítač

        #Zkontroluje a vypíše, kdo vyhrál
        if (ai_bot == "kamen" and clovek == "nuzky") or (ai_bot == "nuzky" and clovek == "papir") or (ai_bot == "papir" and clovek == "kamen"):
            print("Prohrál jsi.")
        elif clovek == ai_bot:
            print("Remíza.")
        else:
            print("Vyhrál jsi.")
        
        #Chceš pokračovat ve hraní?
        check = input("Pokud chceš hrát dál, napiš A, jinak napiš cokoli jiného: ")
        if check.upper() == "A":
            continue
        else:
            break
