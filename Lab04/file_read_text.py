minFil = open ("data/dummytext.txt","r")

fortsett=True
while fortsett:
    linje=minFil.readline()

    if linje=="":
        fortsett=False
    else:
        print(linje)

minFil.close()
