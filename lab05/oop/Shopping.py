from lab05.oop.Butikk import Butikk

bunn_pris = Butikk("Bunnpris")
obs_lade = Butikk("OBS Lade")


#Bestill 500g grønn eple som ikke er importert.
minBestilling = bunn_pris.kjop_vare("EPLE","Grønn",300,"Nei")

for i in range(len(minBestilling)):
    print(minBestilling[i].to_string())
