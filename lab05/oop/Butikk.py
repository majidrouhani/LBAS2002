from lab05.oop.Eple import Eple


class Butikk:
    def __init__(self,navn):
        self.navn = navn
        self.varer = self.eple_lager()

    def eple_lager(self):
        return [
         Eple("Grønn",100,"Nei"),
         Eple("Grønn",120,"Nei"),
         Eple("Grønn",150,"Nei"),
         Eple("Grønn",200,"Nei"),
         Eple("Grønn",110,"Ja"),
         Eple("Rød",90,"Nei"),
         Eple("Rød",201,"Nei"),
         Eple("Rød",220,"Ja"),
         Eple("Rød",190,"Nei"),
         Eple("Gul",180,"Nei"),
         Eple("Gul",280,"Ja"),
         Eple("Gul",380,"Ja"),
         Eple("Gul",170,"Nei")
        ]

    """
    Returnerer en liste med epler der vekten er mindre eller like "vekt"
    som oppfyller farge og om det er importert eller ikke.
    """
    def kjop_vare(selv,vare_navn, farge,vekt,importert):
        kjopte_varer = []
        vare_liste =[]

        totalVekt =0

        if vare_navn == "EPLE":
            vare_liste = selv.varer

        for i in range(len(vare_liste)):
            if (vare_liste[i].get_farge() == farge and
                vare_liste[i].get_importert() == importert and
                totalVekt+vare_liste[i].get_vekt()<vekt):
                totalVekt += vare_liste[i].get_vekt()
                kjopte_varer.append(vare_liste[i])
        return kjopte_varer

