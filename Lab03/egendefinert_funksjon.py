

#Funksjon for å beregne areal til en sirkel
# formel: areal=pi*r*r

def beregnArealSirkel(r):
    areal = 3.14*r*r
    return areal

radius = float(input("Oppgi radius til sirkel: "))

areal = beregnArealSirkel(radius)

print("Arealet til sirkelen med radius ", radius, "er:",areal)

#eller
print("Arealet til sirkelen med radius {0} er: {1}".format(radius,areal))

