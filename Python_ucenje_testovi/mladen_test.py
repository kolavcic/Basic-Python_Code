odgovori = {"Da":"Da", "da":"da"}
name = input("Cao, kako se zoves? ")
print("Cao " + name + "!")
matis = input("Da li zelis da se igramo? ")

def broj (f):
    myfile = open("/Users/kolavcic/Documents/odgovori.txt", encoding = "utf8")
    provera = myfile.read()
    provera = provera.splitlines()
    if f in provera:
        print("Bravo, to je tacan odgovor!")
    else:
        print("Moras jos da ucis!")

if matis in odgovori.keys():
    print("Bravo! Slusaj sada pazljivo!")
    zeli = input("Koliko je 2+2? ")
else:
    print("Bas steta!")

print("Bye Bye!")

myfile = open("/Users/kolavcic/Documents/odgovori.txt", encoding = "utf8")
type(myfile)
myfile.read()
dir(myfile)
#print(provera)