from lab05.oop.Eple import Eple


groennEple = Eple("Grønn",10,"Nei")
roedEple = Eple("Rød",100,"Ja")

print("\n***TEST 1***")
print(groennEple.get_farge())
print(roedEple.to_string())

#Liste med diverse epler
epler = [Eple("Grønn",100,"Nei"),
         Eple("Grønn",120,"Nei"),
         Eple("Grønn",150,"Nei"),
         Eple("Grønn",200,"Nei"),
         Eple("Grønn",110,"Ja"),
         Eple("Rød",90,"Nei"),
         Eple("Rød",201,"Nei"),
         Eple("Rød",220,"Ja"),
         Eple("Rød",190,"Nei")]

"""
Returnerer en liste med epler der vekten er mindre eller like "vekt"
som oppfyller farge og om det er importert eller ikke.
"""
def bestill(list, farge,vekt,importert):
    epler = []
    totalVekt =0
    for i in range(len(list)):
        if (list[i].get_farge() == farge and
            list[i].get_importert() == importert and
            totalVekt+list[i].get_vekt()<vekt):
            totalVekt += list[i].get_vekt()
            epler.append(list[i])
    return epler

print("\n***TEST 2***")

#Bestill 500g grønn eple som ikke er importert.
minBestilling = bestill(epler,"Grønn",2000,"Nei")

for i in range(len(minBestilling)):
    print(minBestilling[i].to_string())
