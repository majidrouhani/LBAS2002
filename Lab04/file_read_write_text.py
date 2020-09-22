inFil = open ("data/dummytext.txt","r")
utFil=open("data/utFil.txt","w")

fortsett=True
while fortsett:
    linje=inFil.readline()

    if linje=="":
        fortsett=False
    else:
        print(linje)
        utFil.write(linje)

inFil.close()
utFil.close()
