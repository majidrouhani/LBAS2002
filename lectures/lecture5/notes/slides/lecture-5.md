---
marp: true
size: 4:3
paginate: true
---
<!-- https://marpit.marp.app/directives -->

# Leksjon 5

**Læringsutbytte**

* Lære å lese fra og skrive til fil
* Lære å koble seg mot MySql database

---
# Filbehandling

Vi kan 
* lagre data på fil 
* lese data fra fil


Når du åpner filen må du spesifisere hvordan du skal bruke filen.
Måten dette gjøres på er som inn-parameter i `open()`-funksjonen, noen eksempler er:

- **'r'** - for lesing av filen (default)
- **'w'** - for skriving til filen
- **'a'** - for å legge til data (**a**ppend) til den eksisterende filen

---

- For å åpne en fil i Python kan vi skrive: `f = open('filename', <Bruksmåte>)`. 
<Bruksmåte> er enten `'r'`, `'w'` eller `'a'` avhengig av hva hvordan filen skal brukes.
- For å lese data fra en fil kan vi bruke: `innhold = f.read()`
- For å legge til data til en fil kan vi skrive: `f.write(data)`
- Filer lukkes på følgende måte: `f.close()`

---
# Lesing fra fil

```python
f = open('example_file1.txt','r') #r spesifiserer at man skal lese fra en fil
innhold = f.read()
print(innhold)
f.close()
```
---
# En bedre måte å lese fra fil

```python
with open('example_file1.txt','r') as f
    innhold = f.read()
    print(innhold)
```
---
# Skriving til fil

```python
f = open('example_file1.txt','w') #w spesifiserer at man skal skrive til en fil (write)
f.write('En hatefull ytring')
f.close()
```
---
# En bedre måte å skrive til fil

```python
with open('example_file1.txt','w') as f
    f.write('En hatefull ytring')
```

---
# Databaser

1. Installer database-pakken for den aktuelle basen (pymysql)
2. En database må eksistere på en database server og du må ha fått tilgang
3. I Python, må du først opprette en kobling mot databasen
4. Deretter leser/oppdaterer du data

---
# Opprett kobling mot databasen

```python
# Database connection object
global db_connection
db_connection = None

my_host = "mysql.stud.iie.ntnu.no"
my_user = "rouhani" # Skriv inn brukernavnet ditt her
my_password = getpass()
my_database = "rouhani"

def get_db_connection():
    if 'db_connection' in globals():
        db_connection = pymysql.connect(host = my_host, 
        user = my_user, 
        password = my_password, 
        database = my_database)
    return db_connection
```

---
# Lese data fra databasen
```python

with get_db_connection() as my_db:
    my_cursor = my_db.cursor()

    my_sql = "SELECT * FROM objects"
    my_cursor.execute(my_sql)

    for row in my_cursor:
        print(row)

```
---
# Legge nye rader med data i databasen
```python

    cursor.execute(f"INSERT INTO objects (giver,...) VALUES({giver}...)")

```

---
# Oppdatere data i databasen
```python

```

---

# Slette data fra databasen
```python

```
