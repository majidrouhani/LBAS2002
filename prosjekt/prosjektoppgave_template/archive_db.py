import pymysql
from tkinter import messagebox
import sys


"""
Skrevet av: Majid Rouhani
Opprettet: 11.09.2018
Oppdatert: 15.10.2019
Versjon: 1.2

Beskrivesle:
Denne modulen leser data fra databasen eller registrerer/oppdaterer gjenstander.
NB! Oppdater variablene user/password slik at de inneholder rett database tilgang.
-----------------------------------------------------------------------------------------------------------
Endret dato, endret av, versjon
<dato>, <navn>, <versjon>
-----------------------------------------------------------------------------------------------------------
"""

my_host = "mysql.stud.iie.ntnu.no"
my_user = "" # Skriv inn brukernavnet ditt her
my_password = "" # Skriv inn passordet ditt her
my_database = "" # Skriv inn database instansen her

def get_db_connection():
    if my_user== "":
        messagebox.showerror("Error", "User/password for database kobling er ikke satt. Sjekk filen archive_db")
        return False
    else:
        return pymysql.connect(host = my_host, user = my_user, password = my_password, database = my_database)


# Søk på gjenstander, gitt navn og/eller registreringsnummer
def search(name, regnr):
    """
    :param name: navn på gjenstand. Denne kan være tom, dvs "" eller være hele/deler av navnet. Case-sensitive!
    :param regnr: registreringsnummer på gjenstand. Denne kan være tom, dvs "" eller være hele/deler av registreringsnummeret. Case-sensitive!
    :return: returnerer en 2-dimensjonal liste med søkeresultater
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    cursor = db.cursor()
    
    # Logger inputdata til konsollet
    print("search: name=" + name + ", regnr=" + regnr)
    sql = "SELECT regnr,navn,regdato,regav FROM gjenstand WHERE navn LIKE '%"+name+"%' AND regnr LIKE '%"+regnr+"%'"
    print(sql)
    cursor.execute(sql)
    
    result = []
    for row in cursor:
        gjenstand = []

        #******************************************
        # Oppgave 4.2
        # Fullfør denne funksjonen slik at en 2-dimensjonal liste (result) returneres
        #******************************************

    db.close()
    
    # Logger antall rader funnet til konsollet
    print("search: rowcount=" + str(len(result)))
    
    return result

#Slett gjenstand
def delete_gjenstand(regnr):
    """
    :param regnr: Registreriongsnr på gjenstand som skal slettes
    :return: ingen returverdi.

    Funksjonen skal finne gjenstanden og slette denne.
    1. Slett fra egenskaper-tabellen for det gitte registreringsnummeret
    2. Slett fra proveniens-tabellen for det gitte registreringsnummeret
    3. Slett fra gjentand-tabellen for det gitte registreringsnummeret

    Dersom sletting går bra, skriv en melding til skjermen.
    """

    #******************************************
    # Oppgave 4.3
    # Fullfør denne funksjonen
    #******************************************

    print("delete_gjenstand: "+regnr)


# Hent alle materialet og antall av hver som to lister
def get_materialet_counts():
    """
    Les antall gjenstander fra databasen gruppert på 'materialet'
    Legg resultatet i to lister: materialet og counts
    :return: counts (liste med tall), materialet (liste med gjenstands materialet)
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    cursor = db.cursor()
    cursor.execute("SELECT count(regnr),materiale FROM egenskaper group by materiale")

    materiale = []
    counts = []
    for row in cursor:
        materiale.append(row[0])
        counts.append(row[1])

    db.close()

    # Logger antall rader funnet til konsollet
    print("get_materialet_counts: rowcount=" + str(len(materiale)))

    return counts, materiale

# Hent all informasjon om en gjenstand basert på regnr
def hent_gjenstand(regnr):
    """
    Henter all informasjon om en gjebstand for en gitt registreringsnr
    :param regnr: Regnr er av typen string
    :return: Returnerer resultatet i en 2-dimensjonal tabell.
             Tabellen vil alltid inneholde en gjenstand da vi søker etter eksakt treff og regnr er primær-nøkkel
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    cursor = db.cursor()

    cursor.execute("""
            SELECT giver,inndato,kommentar,mottattav,navn,plassering,regav,regdato,g.regnr,katnavn,fys_egenskap,maal,materiale,tilstand,produsent,prod_aar,siste_eier,tidl_eiere 
              FROM gjenstand g, 
                   egenskaper e, 
                   kategori k, 
                   proveniens p 
            WHERE g.regnr = e.regnr 
              AND g.kategori_id = k.kategori_id 
              AND g.regnr = p.regnr
              AND g.regnr = %s """, regnr)

    result = []
    for row in cursor:
        print(row)
        gjenstand = []
        for r in range(len(row)):
            gjenstand.append(row[r])
        result.append(gjenstand)

    db.close()

    # Logger antall rader funnet til konsollet
    print("search: rowcount=" + str(len(result)))

    return result

#Get next kategori_id
def get_next_category_id():
    """
    Finn neste kategori_id for registrering av ny gjenstand.
    :return: hente siste kategori_id fra basen og øk tallet med 1. Returner dette
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    cursor = db.cursor()
    cursor.execute("SELECT max(kategori_id) as kategori_id FROM kategori")

    kategori_id = ""

    for row in cursor:
      kategori_id=  str(row[0])

    db.close()

    # Logger antall rader funnet til konsollet
    print("kategori_id: " + kategori_id)

    if int(kategori_id)==0:
        next_kategori_id=1
    else:
        next_kategori_id = int(kategori_id)+1

    return next_kategori_id

#Get next kategori_id
def get_category_id(katnavn):
    """
    :return: hente siste kategori_id fra basen. Returner dette
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    cursor = db.cursor()
    cursor.execute("SELECT kategori_id FROM kategori WHERE katnavn='" + katnavn+"'")

    kategori_id = ""

    for row in cursor:
      kategori_id=  str(row[0])

    db.close()

    # Logger antall rader funnet til konsollet
    print("kategori_id: " + kategori_id)


    return kategori_id


def get_kategori():
    """
    Hent alle kategoriene formatert som dictionary
    :return: kategori liste
    """
    kategori_dic = {}

    db = get_db_connection()

    if not db:
        sys.exit(0)

    cursor = db.cursor()
    cursor.execute("SELECT kategori_id, katnavn FROM kategori")

    for row in cursor:
      kategori_dic.update({row[1]: row[0]})

    db.close()

    return kategori_dic

#Sjekk om regnr existerer i databasen
def regnr_exist(regnr,tabellnavn):
    """
    Sjekk om regnnr existerer allerede i basen
    :param regnr: type string
    :return: boolean
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    cursor = db.cursor()
    sql = "SELECT count(regnr) as regnr_count FROM {0} WHERE regnr='{1}'".format(tabellnavn,regnr)
    cursor.execute(sql)

    regnr_count = 0

    for row in cursor:
      regnr_count=  row[0]

    db.close()

    # Logger antall rader funnet til konsollet
    print("regnr_count: " + str(regnr_count))

    if regnr_count==0:
        return False
    else:
        return True

#Sjekk om kategori_id existerer i basen
def kategori_exist(kategori_id):
    """
    Sjekk om kategori_id existerer i databasen
    :param kategori_id: int
    :return: boolean
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    cursor = db.cursor()
    cursor.execute("SELECT count(kategori_id) as kategori_id_count FROM kategori WHERE kategori_id=%s",kategori_id)

    kategori_id_count = 0

    for row in cursor:
      kategori_id_count=  row[0]

    db.close()

    # Logger antall rader funnet til konsollet
    print("kategori_id_count: " + str(kategori_id_count))

    if kategori_id_count==0:
        return False
    else:
        return True

#Lagrer gjenstand i basen
def save_gjenstand_db(giver_val,
                      innlemmet_dato_val,
                      kategori_id,
                      kommentar_val,
                      mottatt_av_val,
                      navn_val,
                      plassering_val,
                      registrert_av_val,
                      registrerings_dato_val,
                      regnr):
    """
    Lagre gjenstand info i databasen.
    Dersom den finnes allerede, blir gjenstand oppdatert
    Dersom den ikke finnes, blir den opprettet.
    :param giver_val: string
    :param innlemmet_dato_val: string
    :param kategori_id: int
    :param kommentar_val: string
    :param mottatt_av_val: string
    :param navn_val: string
    :param plassering_val: string
    :param registrert_av_val: string
    :param registrerings_dato_val: string
    :param regnr: string
    :return:
    """

    #****************************************
    # Oppgave 4.1
    # Fullfør innholdet i denne funksjonen!
    #****************************************

    # Logger resultatet til konsollet
    #print("save_gjenstand_db: rowcount=" + str(cursor.rowcount))

#Lagre egenskaper til gjenstand
def save_egenskaper_db(fysiske_egenskaper_val,
                       maal_val,
                       materiale_val,
                       regnr,
                       tilstand_val):
    """
    Lagre egenskaper til gjenstand i 'egenskper' tabellen
    :param fysiske_egenskaper_val: string
    :param maal_val: string
    :param materiale_val: string
    :param regnr: string
    :param tilstand_val: string
    :return:
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    db.autocommit(True)
    cursor = db.cursor()

    if regnr_exist(regnr,'egenskaper'):
        cursor.execute("UPDATE egenskaper SET fys_egenskap=%s,maal=%s,materiale=%s,tilstand=%s WHERE regnr=%s",
                   (fysiske_egenskaper_val,maal_val,materiale_val,tilstand_val,regnr))
    else:
        cursor.execute("INSERT INTO egenskaper (fys_egenskap,maal,materiale,regnr,tilstand) VALUES(%s,%s,%s,%s,%s)",
                   (fysiske_egenskaper_val,maal_val,materiale_val,regnr,tilstand_val))

    db.close()

    # Logger resultatet til konsollet
    print("save_egenskaper_db: rowcount=" + str(cursor.rowcount))

#Lagre proveniens til 'proveniens' tabellen
def save_proveniens_db(produsent_val,produksjonsaar_val,regnr,giver_siste_eier_val,tidligere_eiere_val):
    """
    Lagre proveniens i 'proveniens' tabellen i databasen
    :param produsent_val: string
    :param produksjonsaar_val: string
    :param regnr: string
    :param giver_siste_eier_val: string
    :param tidligere_eiere_val: string
    :return:
    """
    db = get_db_connection()

    if not db:
        sys.exit(0)

    db.autocommit(True)
    cursor = db.cursor()

    if regnr_exist(regnr,'proveniens'):
        cursor.execute("UPDATE proveniens SET produsent=%s,prod_aar=%s,siste_eier=%s,tidl_eiere=%s WHERE regnr=%s",
                   (produsent_val,produksjonsaar_val,giver_siste_eier_val,tidligere_eiere_val,regnr))
    else:
        cursor.execute("INSERT INTO proveniens (produsent,prod_aar,regnr,siste_eier,tidl_eiere) VALUES(%s,%s,%s,%s,%s)",
                   (produsent_val,produksjonsaar_val,regnr,giver_siste_eier_val,tidligere_eiere_val))

    db.close()

    # Logger resultatet til konsollet
    print("save_proveniens_db: rowcount=" + str(cursor.rowcount))

