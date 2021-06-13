# Napisati program koji za uneti pozitivan ceo broj n, ispisuje zvezdice i tako iscrtava sledeću sliku:

n = int(input("Unesite broj: "))
star = "*"
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print(f"{star}", end="")
        else:
            print(" ", end="")
    print()

