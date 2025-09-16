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