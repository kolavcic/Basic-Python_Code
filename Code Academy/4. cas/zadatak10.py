# Napisati program koji za uneti pozitivan ceo broj n, ispisuje zvezdice i tako iscrtava odgovarajuću sliku. 
# Slika predstavlja pravougli trougao sastavljen od zvezdica. 
# Kateta trougla je dužine n, a prav ugao nalazi se u gornjem desnom uglu slike.

n = int(input("Unesite broj: "))

for red in range(0, n+1):
    for kolona in reversed(range(0, red)):
        if red == n:
            print("*",end="")
            red = red - 1
    print()