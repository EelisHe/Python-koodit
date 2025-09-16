#1. tehtävä
import math
print("kuhan alamitta on 37cm")
kuha = float(input("minkä pituinen kuha on? : "))
if kuha >= 37:
    print("Onneksi olkoon! voit ottaa kuhan ylös!")
else:
    print("Se on alamittainen. Päästä se takaisin vesistöön.")

#2. tehtävä
hyttiluokka = input("Kertoisitko hyttiluokkasi? : ")
if hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virhellinen hyttiluokka.")

#3. tehtävä
sukupuoli = input("Oletko mies vai nainen? : ")
if sukupuoli == "mies":
    hemoglobiini = int(input("Anna hemoglobiini arvosi (g/l): "))
    if hemoglobiini < 134:
        print("hemoglobiinisi on alhainen")
    elif hemoglobiini > 195:
        print("hemoglobiinisi on korkea")
    elif hemoglobiini >= 134 and hemoglobiini <= 195:
        print("hemoglobiinisi on normaali")
elif sukupuoli == "nainen":
    hemoglobiini = int(input("Anna hemoglobiini arvosi (g/l): "))
    if hemoglobiini < 117:
        print("hemoglobiinisi on alhainen")
    elif hemoglobiini > 175:
        print("hemoglobiinisi on korkea")
    elif hemoglobiini >= 117 and hemoglobiini <= 175:
        print("hemoglobiinisi on normaali")
else:
    print("vastaus ei nyt käy tähän.")

#4. tehtävä
vuosi = int(input("Sano jokin vuosi : "))
if vuosi % 400 == 0:
    print("vuosi on karkausvuosi")
elif vuosi % 100 == 0:
    print("vuosi ei ole karkausvuosi")
elif vuosi % 4 == 0:
    print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")

