n=int(input("Unesite broj n: "))

if n<0:
    print("Greska, neispravan unos")
    exit(1)

ucitani_brojevi = []

for i in range (n):
    ucitani_brojevi.append(int(input("Unesite broj: ")))

suma_negativni_neparni=0

for broj in ucitani_brojevi:
    if broj % 2 != and broj < 0:
        suma_negativni_neparni += broj

print(f"Zbir neparnih negativnih je {suma_negativni_neparni}")