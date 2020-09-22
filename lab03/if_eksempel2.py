import math as m

alder=int(input("Hvor gammel er du?"))
kjonn=input("Oppgi kjønn (J/G): ")


if alder>0 and alder<100 and kjonn=="J":
    print("Du er jente/dame og er mellom 0-100 år gammel!")
elif alder>0 and alder<100 and kjonn=="G":
    print("Du er gutt/mann og er mellom 0-100 år gammel!")
else:
    print("Du har ikke oppgitt riktig data")

