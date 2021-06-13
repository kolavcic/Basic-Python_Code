# Napisati program koji ucitava pozitivan ceo broj n, a potom i n realnih brojeva.
# Program ispisuje koliko puta je prilikom unosa doslo do promene znaka.
# Do promene znaka dolazi kada se nakon pozitivnog unese negativna broj.

n = int(input("Unesite broj n: "))


print("Unesite brojeve: ")
for i in range (n):
    lista_brojeva = []
    brojevi = int(input())
    lista_brojeva.append(brojevi)
    if n<=0:
        print("Greska: neispravan unos.")
        exit(1)

prev = lista_brojeva[0]
ans = 0
  
for element in lista_brojeva:
    if element == 0:
        znak = -1
    else:
        znak = element / abs(element)
    if znak == -prev:
        ans = ans + 1
        prev = znak
  
print(f"Broj promena je {ans}.")

