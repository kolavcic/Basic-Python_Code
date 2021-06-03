moj_broj = int(input("Unesite neki broj: "))

if moj_broj<100:
    print(f"Uneti broj {moj_broj} je manji od 100!")

elif moj_broj>=100 and moj_broj<200:
    print(f"Uneti broj {moj_broj} je veci od 100 i manji od 200!")

elif moj_broj>=200 and moj_broj<300:
    print(f"Uneti broj {moj_broj} je veci od 200 i manji od 300!")

else:
    print(f"Uneti broj {moj_broj} je neki drugi!")