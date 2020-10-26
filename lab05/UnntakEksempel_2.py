
fortsett=True

while fortsett:
    tall1 = int(input("Opp tall 1: "))
    tall2 = int(input("Opp tall 2: "))

    try:
        resultat = tall1/tall2
        fortsett=False
    except ZeroDivisionError:
        print("tall2 kan ikke være 0!")
    except TypeError:
        print("feil data ...")


