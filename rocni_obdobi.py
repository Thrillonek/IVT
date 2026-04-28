mesic = int(input("Zadej číslo měsíce: "))

jaro = (3, 4, 5)
leto = (6, 7, 8)
podzim = (9, 10, 11)
zima = (12, 1, 2)

if mesic in jaro:
    print("Měsíc je na jaře")
elif mesic in leto:
    print("Měsíc je v létě")
elif mesic in podzim:
    print("Měsíc je na podzim")
elif mesic in zima:
    print("Měsíc je v zimě")
else:
    print("Musíte zadat platné číslo měsíce.")
