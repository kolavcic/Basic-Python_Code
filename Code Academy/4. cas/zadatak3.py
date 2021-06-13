# U prodavnici se nalazi n artikala cije su cene pozitivni realni brojevi. Napisati program koji ucitava n,
# a potom i cenu svakog pojedinacnog od n artikala i odredjuje i ispisuje najmanju cenu.

n = int(input("Unesite broj artikla: "))

cene_artikala = []
if n<0:
    print("Greska: neispravan unos.")
    exit(1)

print("Unesite cene artikala: ")
for i in range(n):
    cena_artikla = float(input())
    cene_artikala.append(cena_artikla)
    if cena_artikla<0:
        print("Greska: neispravan unos.")
        exit(2)

print(cene_artikala)
najmanja_cena = min(cene_artikala)
print(f"Najmanja cena: {najmanja_cena:.6f}.")
