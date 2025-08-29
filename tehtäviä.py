#1.tehtävä

nimi = input("anna nimesi: ")
print(f"Moikkelis {"Eelis"}")

#2.tehtävä
import math
sade = float(input("anna ympyrän säde: "))
pinta_ala = math.pi*sade**2
print(f"ympyrän pinta-ala on {pinta_ala:.0f}")

#3.tehtävä
kanta = float(input("anna kanta: "))
korkeus = float(input("anna korkeus: "))
piiri = kanta*2+korkeus*2
print(f"suorakulmion piiri on: {piiri:.0f}")
pinta_ala = kanta*korkeus
print(f"suorakulmion pinta-ala on: {pinta_ala:.0f}")

#4.tehtävä
kokonaisluku1 = float(input("anna kokonaisluku: "))
kokonaisluku2 = float(input("anna kokonaisuluku: "))
kokonaisluku3 = float(input("anna kokonaisluku: "))
summa = kokonaisluku1 + kokonaisluku2 + kokonaisluku3
tulo = kokonaisluku1 * kokonaisluku2 * kokonaisluku3
keskiarvo = (kokonaisluku1 + kokonaisluku2 + kokonaisluku3) / 3
print(f"summa on: {summa:.0f}")
print(f"tulo on: {tulo:.0f}")
print(f"keskiarvo on: {keskiarvo:.0f}")

#5.tehtävä
leiviskat = float(input("anna leiviskat: "))
naulat = float(input("anna naulat: "))
luodit = float(input("anna luodit: "))

kaikkiluodit = (leiviskat * 20 * 32 + naulat * 32 + luodit)
grammat = kaikkiluodit * 13.3
print(f"grammat on: {grammat:.0f} grammaa")
print(f"Massa nykymittojen mukaan on: {grammat // 1000:.0f} kiloa ja {grammat % 1000:.0f} grammaa.")


