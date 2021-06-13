# Napisati program koji ucitava nenegativan ceo broj n i izracunava njegov faktorijel
# U slucaju neispravnog unosa ispistai odgovarajucu poruku o gresci.

n = int(input("Unesite vas broj n: "))
factorial = 1
if n < 0:
       print("Greska: neispravan unos.")
       exit(1)
elif n == 0:
   print("Faktorijel broja 0 je 1.")
else:
   for i in range(1, n+1):
       factorial *=i
   
print(f"{n}! = {factorial}")
