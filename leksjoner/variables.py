'''
Navngiving av variabler: Følg PEP 8 standarden:
https://www.python.org/dev/peps/pep-0008/

- Bare små bokstaver
- Ikke norske tegn eller andre spesial tegn
- Ikke tillatt med mellomrom
- Bruk alltid beskrivende navn

'''

#Eksempel: feil måte å definere variabler på
#a = 25
#A=26
#maks antall=10
#MaksAntall=10
#Anders’ leilighet = '2a'

#Eksempel: riktig måte å definere variabler på
age = 25
max_number = 10
message = 'Hello World'
appartment_no = '2a'

print(str(age)+' '+str(max_number)+' '+message)


postnummer = '0125'
poststed = 'Oslo'
gate_adresse = 'Olav Magnussons veg'

adresse = gate_adresse+"\n"+postnummer+" "+poststed

print(adresse)



