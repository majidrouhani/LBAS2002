import lab04.min_statistikk_pakke.statistikk as stat
import lab04.min_statistikk_pakke.matematikk as matte

def test():
    #Test 1: heltall
    tall = 4
    resultat = matte.opphoydI(tall, 2)
    print("Test 1: ",resultat)

    #Test 2: flyttall
    tall = 4.2
    resultat = matte.opphoydI(tall, 2)
    print("Test 2: ",resultat)

    #Test 3: Ugyldig tall
    tall = '4'
    resultat = matte.opphoydI(tall, 2)
    print("Test 3: ",resultat)

    #Test 4: Liste
    tall = [2,4,6]
    resultat = matte.opphoydI(tall, 2)
    print("Test 4: ",resultat)

    #Test 5: Liste med et ugyldig tall
    tall = [2,4,'7',6]
    resultat = matte.opphoydI(tall, 3)
    print("Test 5: ",resultat)

    #Test 6: gjennomsnitt
    tallListe = [2,4,6]
    gjennomsnitt = stat.gjennomsnitt(tallListe)
    print("Test 6: ",gjennomsnitt)

    #Test 7: gjennomsnitt
    nyTallListe = matte.opphoydI(tallListe, 4)
    gjennomsnitt = stat.gjennomsnitt(nyTallListe)
    print(f"Test 7: {gjennomsnitt:0.2f}")


test()


