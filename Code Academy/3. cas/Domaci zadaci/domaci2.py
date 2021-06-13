# Napisati program koji ucitava realan broj x i ceo nenegativan broj n i izracunava n-ti stepen broja x.
# U slucaju neispravnog unos ispisati odgovarajucu poruku o gresci.

# x, n = map(int, input("Unesite redom brojeve x i n: ").split())
x=int(input("Unesite broj x: "))
n=int(input("Unesite broj n: "))

if n<0:
    print("Greska: neispravan unos broja n.")
    exit(1)
#else:
    #print(f"Rezultat: {x^n:.5f}")

rezultat=1

for i in range (n):
    rezultat *= x

print(rezultat)   