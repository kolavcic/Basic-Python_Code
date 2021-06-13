#Ovaj program treba da vrati da ispise broj dana u nedelji ukoliko je uneti broj 1-7, 
# i da ispise gresku ukoliko je uneti broj veci od 7.

moj_broj = int(input("Unesite broj dana u nedelji: "))

if moj_broj==1:
    print(f"Korisnik je uneo {moj_broj} i to je: ponedeljak!")
elif moj_broj==2:
    print(f"U pitanju je: utorak!")
elif moj_broj==3:
    print(f"U pitanju je: sreda!")
elif moj_broj==4:
    print(f"U pitanju je: cetvrtak!")
elif moj_broj==5:
    print(f"U pitanju je: petak!")
elif moj_broj==6:
    print(f"U pitanju je: subota!")
elif moj_broj==7:
    print(f"U pitanju je: nedelja!")
else:
    print(f"Greska: neispravan unos dana.")