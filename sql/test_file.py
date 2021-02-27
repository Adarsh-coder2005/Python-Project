import psycopg2

conn = psycopg2.connect("dbname=project user=postgres password=AD784521")
cursor = conn.cursor()

cursor.execute("Select * from bank")
rows = cursor.fetchall()

for row in rows:
    print(row)
cursor.close()

bank = conn.cursor()

bank.execute("Select * from branch")
rows = bank.fetchall()

for row in rows:
    print(row)
bank.close()
conn.close()