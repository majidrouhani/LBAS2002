import pymysql

host = "mysql.stud.iie.ntnu.no"
user = "rouhani" # Skriv inn brukernavnet ditt her
password = "mPZSMTaw" # Skriv inn passordet ditt her


conn= pymysql.connect(host, user, password, user)
cursor = conn.cursor()

sql = "SELECT 'Dette er en test!' FROM dual"

cursor.execute(sql)

for row in cursor:
    print(row[0])

conn.close()

