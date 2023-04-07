---
marp: true
size: 4:3
paginate: true
---
<!-- https://marpit.marp.app/directives -->

# Leksjon 2

**Læringsutbytte**

* Kunne skrive enkle matematiske uttrykk i Python
* Lære å definere funksjoner i Python
* Kunne sette opp logiske uttrykk
* Lære å bruke if-setningen i Python.

---
# Funksjoner og kalkulasjoner

**Aritmetikk**

**Presedens mellom operatorer fungerer som i matematikken.**

* Multiplikasjon og divisjon har høyere presedens enn addisjon og subtraksjon.
* 3 + 2 * 5 blir 13, fordi * gjøres før +.
* 5 - 1 / 2 blir 4.5, fordi / gjøres før -.
* Potens har høyere presedens enn multiplikasjon og divisjon:
    5 * 2 ** 3 blir 40, fordi ** gjøres før *.
---
* Parenteser kan brukes for å få en annen rekkefølge på regneoperasjonene:
    * (3 + 2) * 5 blir 25, fordi + gjøres før *.
    * (5 - 1) / 2 blir 2, fordi - gjøres før /.
    * (5 * 2) ** 3 blir 343, fordi * nå gjøres før **.
* Hvis du skal "oversette" et matematisk uttrykk med parenteser til Python, bruk parenteser på samme sted også i Python-koden.

---

## Funksjoner

Eksempel på den matematiske funksjonen $f(x) = 2x + 3$ i Python:

```python
def f(x): # Definerer funksjonen
    return 2 * x + 3 # Returnerer parameteren x ganget med 2 og plusset med 3


# Kall/bruk funksjonen    
print(f(1))
print(f(2))

y = f(3)
print(y)
```
---
# Moduler og pakker

* En modul i Python er en python-fil
* En modul inneholder python-code, som regel funksjoner.
* Eksempel på en modul er 'math'
* Vi kan bruke moduler i våre programmer:
```python
import math

print(math.pi) # printer ut verdien av variabelen pi som ligger i modulen math
print(math.pow(4,2)) # printer 4*4 = 16
```
```python
import math as m

print(m.pi) # printer ut verdien av variabelen pi som ligger i modulen math
print(m.pow(4,2)) # printer 4*4 = 16
```

---

```python
from math import pi, pow

print(pi) # printer ut verdien av variabelen pi som ligger i modulen math
print(pow(4,2)) # printer 4*4 = 16
```
---
# Pakker

* Pakker består av flere moduler
* Vi kan importere hele eller deler av en pakke
* De fleste pakkene må installeres i miljøet før de kan tas i bruk.
* På Jupyter har vi allerede installert det meste av det som trengs i dette kurset.
* For å installere en pakke, start terminal vindu og skriv:

```python
pip install <<pakkenavn>>
```

Eksempel:
```python
pip install matplotlib
```
---

# Eksempler på bruk av pakker

```python
import matplotlib.pyplot as plt
import random as rnd

dager = range(7)
regn_mm = [rnd.randint(0,10) for i in dager]

plt.plot(dager,regn_mm)
```

---
## Logiske operatorer

* `==` (betyr "er lik", merk at her er to likhetstegn nødvendig for å skille fra tilordningsoperatoren)
* `!=` (betyr "ulik", altså det motsatte av ==)
* `>` , `<` , `>=` , `<=` (som betyr henholdsvis større, mindre, større eller lik, og mindre eller lik)

```python
a = 10
b = 15

er_lik = a == b
print (er_lik)

er_storre = a > b
print (er_storre)

er_ulik = a != b
print (er_ulik)
```

---
# if-setninger

* Bruker til å finne ut resultatet av logiske uttrukk blir

```python
a = 10
b = 15

if a == b:
    print ('a er lik b')

if a > b
    print ('a er større enn b')

if a != b:
    print ('a er ulik b')
```