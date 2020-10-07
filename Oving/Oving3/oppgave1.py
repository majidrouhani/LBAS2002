
utFil=open("utFil.txt","w")

fortsett=True
setningListe = []

while True:
    setning = input("Skriv inn en setning: ")
    if setning == "-1":
        break
    else:
        setningListe.append(setning)

print("Skriver til fil")

#Alternativ 1
utFil.write("Alternativ 1: \n")
for i in range(0,len(setningListe)):
    utFil.write(setningListe[i]+"\n")


#Alternativ 2
utFil.write("\nAlternativ 2:")
utFil.write("\n".join(setningListe))

utFil.close()
