# U prodavnici se nalaze artikli cije su cene pozitivni realni brojevi.
# Napisati program koji ucitava cene artikala sve do unosa broja nula i izracubava i ispisuje prosecnu
# vrednost cena u radnji. U slucaju neispravnog unosa, ispisati odgovarajucu poruku o gresci.

n = int(input("Unesite broj cena: "))

if n<0:
    print("Greska: neispravan unos cene.")
    exit(1)

elif n ==0:
    print("Nisu unete cene.")
    exit(2)

else:
    cene = []
    print("Unesite cene: ")
    for i in range(n):
        cena = float(input())
        cene.append(cena)
        if cena<0:
            print("Greska: neispravan unos cene.")
            exit(3)
        if cena==0:
            print("Nisu unete cene.")
            exit(4)
zbir = sum(cene)

print(f"Prosecna cena: {zbir/n:.4f}.")