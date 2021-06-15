# Napisati program koji za uneti pozitivan ceo broj n, ispisuje veliko plus dimenzije n:

n = int(input("Unesite broj: "))
plus = "+"
for red in range(n):
    for kolona in range(1 ,n+1):
        if red==n or kolona==n:
            print(f"{plus}", end="")
        elif kolona 
        else:
            print(" ", end="")
    print()