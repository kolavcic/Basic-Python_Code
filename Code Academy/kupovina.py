cena_hleba = int(input("Unesite cenu hleba: "))
kolicina = int(input("Unesite kolicinu: "))
iznos = int(input("Unesite iznos placanja: "))

kusur = iznos - cena_hleba*kolicina

print(f"Kusur koji kasirka treba vrati iznosi {kusur} dinara.")