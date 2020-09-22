
"""
Innparameter:
tall: kan være heltall, desimaltall eller en liste med tall.
potens: er heltall
"""
def opphoydI(tall,potens):
        nyListe = []

        if type(tall) is int or type(tall) is float:
                return pow(tall,potens)
        elif type(tall) is str:
                return None
        else:
                n = len(tall)
                for i in range(len(tall)):
                        detteTallet = tall[i]
                        if type(detteTallet) is int or type(detteTallet) is float:
                                nyListe.append(pow(tall[i],potens))
                        elif type(detteTallet) is str:
                                 nyListe.append(None)
        return nyListe
