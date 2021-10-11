import pymysql

my_host = "mysql.stud.iie.ntnu.no"
my_user = "rouhani" # Skriv inn brukernavnet ditt her
my_password = "mPZSMTaw" # Skriv inn passordet ditt her
my_database = "rouhani"



conn= pymysql.connect(host=my_host, user=my_user, password=my_password, database=my_database)
cursor = conn.cursor()

sql = "SELECT * FROM kategori"

cursor.execute(sql)

for row in cursor:
    print(row[0],row[1])

conn.close()

