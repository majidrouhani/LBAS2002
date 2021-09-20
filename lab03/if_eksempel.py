alder = int(input("Hvor gammel er du?"))
kjonn = input("Skriv kjønn:")
foler_som_ungdom = True

if (alder>13 and alder<34) or foler_som_ungdom:
    print("Du er ungdom, gutt!")

if alder<0 or alder>130:
    print("Du har oppgitt ugyldig alder!")
    print("Prøv igjen.")
elif kjonn == "G":
    print("Du er gutt. Gyldig alder:",alder)
    print("Flink gutt!")
elif kjonn == "J":
    print("Du er jente. Gyldig alder:",alder)

print("Programmet er slutt!")