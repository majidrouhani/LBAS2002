
#Eksempel 1: skriv ut tallene mellom 0 og 10.
for i in range(0,10):
    print(i)


#Eksempel 2: Skriv ut innholdet i listen:
min_liste = [25,"Ola Norman", "Bakkelandet"]
print(min_liste)

for i in min_liste:
    print(i)

#Eksempel 3: Skriv ut innholdet i listen med en "prefiks"
min_liste = [25,"Ola Norman", "Bakkelandet"]
n=0
for i in min_liste:
    n=n+1
    print("Element nr ",n,":",i)


#Eksempel 4: Skriv et program som regner ut summen av tallene fra og med 1 til og med 449 ved hjelp av en for-løkke, og til slutt printer ut resultatet
sum = 0
number = range(1,45)
for i in number:
    sum = sum + i

print(sum)
