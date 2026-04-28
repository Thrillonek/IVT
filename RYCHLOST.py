while True:
    rychlost = int(input("JAK CHODÍŠ RYCHLE? "))
    if rychlost <= 5:
        print("MUSÍŠ ZRYCHLIT")
    elif rychlost > 8:
        print("ZPOMAL")
    else:
        print("JEN TAK DÁL")
    print("\n")