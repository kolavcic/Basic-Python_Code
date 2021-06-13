broj=int(input("Unesite ceo broj: "))

cifre = []

# if broj > 0:
#     apsolutna_vrednost = broj
# else:
#     apsolutna_vrednost = broj * -1

apsolutna_vrednost = abs(broj)

while apsolutna_vrednost != 0:
    cifre.append(apsolutna_vrednost%10)
    apsolutna_vrednost//=10
    
print(cifre)

