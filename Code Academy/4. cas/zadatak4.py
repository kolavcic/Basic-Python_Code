# Napisati program koji uneti pozitivan ceo broj transformise tako sto svaku parnu cifru
# u zapisu broja uveca za jedan. Ispisati dobijeni broj.

n = int(input("Unesite broj: "))

if n<=0:
    print("Greska: neispravan broj.")
    exit(1)

for i in str(n):
    if int(i) % 2==0:
        i += 1
        