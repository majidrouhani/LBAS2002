


mine_tall = []

fortsett = True

while fortsett:
    tall = float(input("Oppgi et tall: "))
    if tall == -1:
        fortsett = False
    else:
       mine_tall.append(tall)

print(mine_tall)
