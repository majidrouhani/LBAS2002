
def minSum(liste):
    return sum(liste)

def gjennomsnitt(liste):
    lengde = len(liste)
    sumListe = sum(liste)

    if lengde>0:
        return sumListe/lengde
