broj = int(input("Unesite pozitivan broj: "))

cifre = []

if broj <= 0:
    print("Greska: neispravan ulaz.")
    exit(1)

# 123
# [3, 2, 1]

broj_za_obradu = broj

while broj_za_obradu != 0:
    cifre.append(broj_za_obradu%10)
    broj_za_obradu//=10

#suma_cifara = 0

# for cifra in cifre:
#     suma_cifara += cifra

suma_cifara=sum(cifre)

if broj % suma_cifara ==0:
    print(f"Broj {broj} je deljiv sa {suma_cifara}")
else:
    print(f"Broj {broj} nije deljiv sa {suma_cifara}")
