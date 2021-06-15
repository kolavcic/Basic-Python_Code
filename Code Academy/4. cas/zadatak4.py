# Napisati program koji uneti pozitivan ceo broj transformise tako sto svaku parnu cifru
# u zapisu broja uveca za jedan. Ispisati dobijeni broj.

n = int(input("Unesite broj: "))

novi_broj = []

if n<=0:
    print("Greska: neispravan broj.")
    exit(1)

for i in str(n):
    i = int(n)
    i += 1
    while i % 2==0:
        novi_broj.append(i)
print (novi_broj)
