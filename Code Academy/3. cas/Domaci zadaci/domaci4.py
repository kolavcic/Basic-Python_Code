n=int(input("Unesi neki broj: "))

privremena_promenljiva = n

while privremena_promenljiva % 10 == 0 and privremena_promenljiva !=0:
    privremena_promenljiva //=10

print(privremena_promenljiva)

# 147 % 10 = 7 uzimamo poslednju cifru
# 147 // 10 = skidamo poslednju cifru
