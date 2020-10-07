from lab05.oop.Butikk import Butikk

bunn_pris = Butikk("Bunnpris")


print("\n***TEST 2***")

#Bestill 500g grønn eple som ikke er importert.
minBestilling = bunn_pris.kjop_vare("EPLE","Grønn",2000,"Ja")

for i in range(len(minBestilling)):
    print(minBestilling[i].to_string())
