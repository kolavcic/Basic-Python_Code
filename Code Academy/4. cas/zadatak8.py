# Napisati program koji za uneti pozitivan ceo broj n, ispisuje veliko plus dimenzije n:

n = int(input("Unesite broj: "))
plus = "+"
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==n:
            print(f"{plus}", end="")
        else:
            print(" ", end="")
    print()