vaha = int(input("Sděl mi svou váhu v kg: "))
vyska = int(input("Sděl mi svou výšku v cm: "))

bmi = vaha/(vyska*0.01)**2

if bmi < 18.5:
    print("Podvýživené africké dítě")
elif bmi > 25:
    print("Průměrný americký mc\'doland enjoyer")
else:
    print("člověk")
