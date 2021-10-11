
fortsett = True

while fortsett:
    try:
        tall_1 = float(input("Tall 1: "))
        tall_2 = float(input("Tall 2: "))

        resultat = tall_1 / tall_2
        fortsett = False
    except ValueError:
        print("Vennligst oppgi et TALL")
    except ZeroDivisionError:
        print("Tall 2 kan ikke være 0")


print(tall_1,"/", tall_2," = ",resultat)