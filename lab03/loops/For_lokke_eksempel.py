
#Eksempel 1: skriv ut tallene mellom 0 og 10.
for i in range(0,100,10):
    print("i = ",i)
    print("i * i = ",i*i)

#Eksempel 2: Skriv ut innholdet i listen:
min_liste = [25,"Ola Norman", "Bakkelandet"]
print(min_liste)

for element in min_liste:
    print(element)

print(element)

#Eksempel 3: Skriv ut innholdet i listen med en "prefiks"
min_liste = [25,"Ola Norman", "Bakkelandet"]
n = 0
for i in min_liste:
    n += 1
    print("Element nr ",n,":",i)


#Eksempel 4: Skriv et program som regner ut summen av tallene fra og med 1 til og med 449 ved hjelp av en for-løkke, og til slutt printer ut resultatet
sum = 0
number = range(0,45000,2)
for i in number:
    sum = sum + i

print(sum)


liste = [0,10,20,30,40,50,100,200,400]

s = 0
for n in liste:
    s+=n

print("Summen er: ",s)