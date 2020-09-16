#Vi kan velge om vi vil jobbe med heltall eller desimaltall.
#I denne løsningen har vi valgt å jobbe med desimaltall (float)

tallListe = []

tall1 = float(input("Oppgi tall 1: "))
tall2 = float(input("Oppgi tall 2: "))
tall3 = float(input("Oppgi tall 3: "))
tall4 = float(input("Oppgi tall 4: "))

tallListe.append(tall1)
tallListe.append(tall2)
tallListe.append(tall3)
tallListe.append(tall4)

#Sorter og skriv ut
tallListe.sort()
print("Tall:",tallListe)

#Summer og skriv ut
sumTall = sum(tallListe)
print("Sum:",sumTall)

#Beregn gjennomsnitt og skriv ut
antall = len(tallListe)
if (antall>0):
    gjennomsnitt = sumTall/antall

    print("Gjennomsnitt: ",gjennomsnitt)
