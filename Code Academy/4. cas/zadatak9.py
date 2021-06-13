# Napisati program koji za uneti pozitivan ceo broj n, ispisuje zvezdice i tako iscrtava odgovarajuću sliku. 
# Slika predstavlja pravougli trougao sastavljen od zvezdica. 
# Kateta trougla je dužine n, a prav ugao nalazi se u gornjem levom uglu slike.

n = int(input("Unesite broj: "))

for i in reversed(range(0, n)):
    for j in reversed(range(0, i+1)):
            print("*",end="")
    print()

