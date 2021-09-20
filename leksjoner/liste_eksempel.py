
person_register_liste = []

def les_info():
    person_info_liste = []
    navn = input("Hva heter du?")
    person_info_liste.append(navn)

    alder = input("Hvor gammel er du?")
    person_info_liste.append(alder)

    studie = input("Hva studerer du?")
    person_info_liste.append(studie)

    person_register_liste.append(person_info_liste)


les_info()
les_info()
les_info()

print(person_register_liste)
