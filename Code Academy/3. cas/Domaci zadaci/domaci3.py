pravi_delioci = []
n=int(input("Unesite pozitivan ceo broj n: "))

if n<0:
    print("Greska: neispravan unos.")

else:
    for i in range(2,n):
        if n % i == 0:
            pravi_delioci.append(i)
    
print(pravi_delioci)

