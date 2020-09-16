import math as m

#Funksjon for å beregne areal til en sirkel
# formel: areal=pi*r*r

def beregnArealSirkel(r):
    areal = m.pi*m.sqrt(r)
    return areal

radius = float(input("Oppgi radius til sirkel: "))

areal = beregnArealSirkel(radius)

print(f"Arealet til sirkelen med radius {radius} er: {areal:0.5f}")

#eller
print("Arealet til sirkelen med radius {0} er: {1:0.3f}".format(radius,areal))
