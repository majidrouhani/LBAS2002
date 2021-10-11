min_fil = open ("./data/dummytext.txt", "r")

fortsett=True
while fortsett:
    linje=min_fil.readline()

    if linje=="":
        fortsett=False
    else:
        print(linje)

min_fil.close()
