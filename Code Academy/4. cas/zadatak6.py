# Napisati program koji za uneti pozitivan ceo broj n, ispisuje zvezdice i tako iscrtava sledeću sliku

n = int(input("Unesite broj: "))
star = "*"
for i in range(n):
    for j in range(n):
        print(f"{star}", end="")
    print()

