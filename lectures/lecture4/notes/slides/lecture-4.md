---
marp: true
size: 4:3
paginate: true
---
<!-- https://marpit.marp.app/directives -->

# Leksjon 4

**Læringsutbytte**

* Lære å lage lister og manipulere elementene i en gitt liste.
* Slicing av lister


---

# Lister

* For å opprette en tom liste i Python skriver vi []
* Lister elementene kan være av forskjellige typer

```python
min_liste = [4,'elementer','i','listen']
```

Denne listen består av heltall (int) og strenger (str).

---

# Lister og inneholde andre lister

* Et element i en liste kan være en annen liste

```python
frukt_liste = ['Banana', 'Appelsin', 'Eple']
gronnsak_liste = ['Gullrot','Asparges', 'Purreløk','Salat']
div_liste = ['Kjøttdeig', 'Makaroni', 'Salt']

handleliste = ['Handleliste for 08.04.2023',frukt_liste, gronnsak_liste, div_liste]

handleliste[0] # Printer Handleliste for 08.04.2023
handleliste[1] # Printer ['Banana', 'Appelsin', 'Eple']
handleliste[1][2] # Printer Eple
```

---
# Lister og løkker

For å iterere/gå gjennom elementene i en liste brukes løkker, og dette gjøres hovedsakelig på to ulike måter:

1. For-løkker, ved å bruke range()-funksjonen og indekser.

```python
liste = [1,2,3,4,5]
for x in range(len(liste)):
    print(liste[x])
```

2. For-in-løkker, som henter ut ett og ett element av en liste.

```python
liste = [1,2,3,4,5]
for x in liste:
    print(x)
```    

---
# Kopiering av lister

```python
frukt_liste = ['Banana', 'Appelsin', 'Eple']
gronnsak_liste = ['Gullrot','Asparges', 'Purreløk','Salat']
div_liste = ['Kjøttdeig', 'Makaroni', 'Salt']

handleliste_1 = ['Handleliste for 08.04.2023',frukt_liste, gronnsak_liste, div_liste]
handleliste_2 = handleliste_1
handleliste_2[0] = 'Handleliste for 09.04.2023' # Handleliste_1 er også endret!

handleliste_3 = handleliste_1[:] # 'Showllow' kopi
handleliste_3[0] = 'Handleliste for 09.04.2023' # Handleliste_1 blir ikke endret!

handleliste_1[1].append('Druer')
handleliste_3   #Handleliste_3 inneholder Druer også! (Pga showllow kopiering)
```

---
# Dyp kopiering

Dyp kopiering kopierer også underliggende objekter (i motsetning til shallow som bare kopierer referanser til underliggende objekter)

```python
import copy

handleliste_4 = copy.deepcopy(handleliste_1)

handleliste_1[2].append('Tomat')

(handleliste_1, handleliste_4)
```

Her vil handleliste_4 ikke inneholde 'Tomat'

---
# Tupler

Er det samme som lister med den forskjellen at de ikke kan endres. Bruker paranteser når vi definerer dem

```python
ukedager = ('mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag', 'søndag')
```

Det er f.eks. ikke lov å skrive:
```python
ukedager[0] = 'tirsdag'
```

---
# Set

Er det samme som lister med den forskjellen at elementene kan forekomme bare en gang (unike verdier). Bruker krøll-paranteser når vi definerer dem
