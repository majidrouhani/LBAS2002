


mine_tall = []

while True:
    try:
        tall = float(input("Oppgi et tall: "))
        if tall == -1:
            break
        else:
           mine_tall.append(tall)
    except ValueError as err:
        print("Ugyldig input!",err, "Prøv igjen")

print(mine_tall)
