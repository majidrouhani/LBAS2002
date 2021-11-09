"""
Programmet tar i mot setninger fra bruker og lagrer disse i fil
"""

ut_fil=open("utFil.txt", "w")

fortsett=True
setning_liste = []

while True:
    setning = input("Skriv inn en setning: ")
    if setning == "-1":
        break
    else:
        setning_liste.append(setning)

print("Skriver til fil")

#Alternativ 1
ut_fil.write("Alternativ 1: \n")
for i in range(0, len(setning_liste)):
    ut_fil.write(setning_liste[i] + "\n")


#Alternativ 2
ut_fil.write("\nAlternativ 2:")
ut_fil.write("\n".join(setning_liste))

ut_fil.close()
