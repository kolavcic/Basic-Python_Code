# Ovaj program treba da trazi od Korisnika unos 2 broja, i kasnije da izvrsi osnovne matematicke radnje.

print("Zdravo! Ovo je zabavan program, koji je napravljen da bi se vezbao python.")

# Korisnik unosi svoje ime.
ime = input("Kako se zoves? ")

# Korisnik unosi prvi broj.
tekst1 = input("Zdravo " + ime + "," + " unesi prvi broj: ")
# Funkcija osigurava da korisnik moze uneti samo broj u prethodnom koraku.
broj1 = int(tekst1)

# Korisnik unosi drugi broj.
tekst2 = input("Sada " + ime + " unesi drugi broj: ")
# Funkcija osigurava da korisnik moze uneti samo broj u prethodnom koraku.
broj2 = int(tekst2)

#Varijabla koja se koristi kasnije u kodu.
korisnik = "koje si uneo iznosi:"

# Prikaz brojeva koje je korisnik uneo.
print(ime + " uneo si brojeve", broj1, "i", broj2)

# Racunanje zbira brojeva koje je korisnik uneo.
print("Zbir brojeva " + korisnik, broj1 + broj2)

# Racunanje razlike brojeva koje je korisnik uneo.
print("Razlika brojeva " + korisnik, broj1 - broj2)

#Racunanje mnozenja brojeva koje je korisnik uneo.
print("Proizvod brojeva " + korisnik, broj1 * broj2)

#Racunanje deljenja brojeva koje je korisnik uneo.
print("Kolicnik brojeva "  + korisnik, broj1 // broj2)
print(type(korisnik))