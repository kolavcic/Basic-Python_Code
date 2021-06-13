# Napisati program koji učitava ceo broj n, a zatim i n karaktera. 
# Program treba da proverava da li se od unetih karaktera može napisati reč Zima. 
# U slučaju neispravnog unosa, ispisati odgovarajuću poruku o grešci.

n = int(input("Unesite broj n: "))

rec = ["Z","i","m","a"]

karakteri = []

if n<=0:
    print("Greska: neispravan unos.")
    exit(1)

for i in range(1,n+1):
        slovo = str(input(f"Unesite {i}. karakter."))
        karakteri.append(slovo)
if slovo in rec:
    print("Moze se napisati rec Zima.")
else:
    print("Ne moze se napisati rec Zima.")
    

    