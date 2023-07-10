import mysql.connector as mysql

# db = mysql.connect(host = 'localhost', port =3306, user='root', password='SauravMysql1!')
# print(db)

# cursor = db.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS ds2022")
# db.commit()

# dbs = cursor.fetchall()
# for db in dbs:
#     print(db)

db = mysql.connect(host = 'localhost', port =3306, user='root', password='SauravMysql1!', database='ds2022')
cursor = db.cursor()
query = 'select * from gold_price'

cursor.execute(query)
records = cursor.fetchall()
for record in records:
    print(record)

db = mysql.connect(host = 'localhost', port =3306, user='root', password='SauravMysql1!', database='ds2022')
cursor = db.cursor()
query = "insert into gold_price values('2023-01-03', 1294.0)"
values = ("1980.0")

cursor.execute(query)
db.commit()
print(f"{cursor.rowcount} records inserted into gold_price")
