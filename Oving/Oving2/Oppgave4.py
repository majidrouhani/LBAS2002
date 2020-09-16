import Oving.Oving2.statistikk as minStat

tallListe = []

while True:
    tall =float(input("Oppgi et tall (-1 for å avslutte): "))
    if tall ==-1:
        break
    else:
        tallListe.append(tall)


print("Du skriv inn: ", len(tallListe)," tall!")
print("Sum:",minStat.minSum(tallListe))
print("Gjennomsnitt:",minStat.gjennomsnitt(tallListe))
