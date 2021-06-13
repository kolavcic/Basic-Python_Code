t=int(input("Unesite broj transakcija: "))

if t<0:
    print("Greska: neispravan unos.")
elif t==0:
    print("Nema evidentiranih transakcija.")
else:
    transakcije = []
    print("Unesite transakcije: ")
    for i in range(t):
        ucitan_broj = int(input())
        transakcije.append(ucitan_broj)

#   print(transakcije)

    prihod=0
    rashod=0

    for transakcija in transakcije:
        if transakcija<0:
            rashod += transakcija
        else:
            prihod += transakcija

print(f"Prihod: {prihod}")
print(f"Rashod: {rashod}")

zarada_ili_gubitak = prihod + rashod
if zarada_ili_gubitak >=0:
        print(f"Zarada: {zarada_ili_gubitak}")
else:
        print(f"Gubitak: {zarada_ili_gubitak}")
