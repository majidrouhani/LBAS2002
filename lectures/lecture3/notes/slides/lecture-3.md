---
marp: true
size: 4:3
paginate: true
---
<!-- https://marpit.marp.app/directives -->

# Leksjon 3

**Læringsutbytte**

* Lære å sammenligne strenger og bruk av if

---

## Sammenligning av strenger

* Når man sammenligner to strenger i Python vil strengene sammenlignes karakter for karakter
* Hver karakter har et tallverdi (ascii-kode):
    * A = 65, B = 66, ..., Z = 90, a = 97, ..., z = 122
    * '0' = 48, ..., '9' = 57


```python
ord('A') # prints Unicode code for A, which is 65 (ordinal value)

chr(65) # prints letter A
```

---
## Hvordan skjer sammenligning?

Anta vi har to strenger s1 og s2.

1. Første tegnet i hver streng sammenlignes. \
Hvis Unicode verdien i s1[0] er større enn s2[0], er s1 større
1. Hvis s1[0] == s2[0], sammenlignes s1[1] med s2[1]. \
Slik fortsetter det inntil et avvik finnes, eller vi er ferdige
1. Hvis strengene er like, er den lengste større

```python
student_one = "Penny"
student_two = "Paul"

if student_one > student_two:
	print(f"{student_two} comes before {student_one} in the alphabet.")
elif student_one < student_two:
	print(f"{student_one} comes before {student_two} in the alphabet.")
```

---
# Introduksjon til løkker

![Loops](https://www.incredible-web.com/media/7242/loops.png)


---

```python
print("Hipp Hipp Hurra!",1)
print("Hipp Hipp Hurra!",2)
print("Hipp Hipp Hurra!",3)
print("Hipp Hipp Hurra!",4)
print("Hipp Hipp Hurra!",5)
print("Hipp Hipp Hurra!",6)
print("Hipp Hipp Hurra!",7)
print("Hipp Hipp Hurra!",8)
print("Hipp Hipp Hurra!",9)
print("Hipp Hipp Hurra!",10)

for tell in range(1,11):
    print("Hipp Hipp Hurra!",tell)
    
```
---
# Nøstede løkker

* Løkker i løkker
* Eksempler på situasjoner der vi kan få bruk for nøstede løkker:
  * Vi har 60 sekunder i et minutt, 60 minutter i en time, 24 timer i et døgn osv.
  * Vi har en 2-dimensjonal tabell med kolonner og rader (looper gjennom rader og for hver rad, looper gjennom kolonner)


---

```python
def format_card_deck():
    
    farger = ['♠', '♣', '♥', '♦']
    verdier = ['A', '2', '3', '4', '5', '6', '7', '8',
                  '9', '10', 'J', 'Q', 'K']
    outer_string = ""
    
    for farge in farger: 
        inner_string = ""
        for verdi in verdier:
            inner_string += farge + verdi + " "
        outer_string += inner_string + "\n"
           
    return outer_string

print(format_card_deck())
```