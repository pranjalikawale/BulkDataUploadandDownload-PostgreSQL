import psycopg2
import csv

conn=psycopg2.connect(database="testdb", user = "postgres", password = "123", host = "127.0.0.1", port = "5432")
print("Opened database successfully")
cur = conn.cursor()
cur.execute('''
            CREATE table Baller(sr_no int PRIMARY KEY NOT NULL, 
                                player varchar(40) NOT NULL )
            ''')
with open('C:\\Users\\User\\Desktop\\python\\Postgress_DB\\baller.csv', 'r') as file_name:
    reader = csv.reader(file_name)
    next(reader) # Skip the header row.
    for row in reader:
        cur.execute(
        "INSERT INTO Baller VALUES (%s, %s)",row
    )

# Operation Display
cur.execute("SELECT * FROM Baller")
rows = cur.fetchall()
print("\nSr_No\t NAME")
for row in rows:
   print(f"{row[0]}\t {row[1]}") 
conn.commit()
print("Operation done successfully")
cur.close()
conn.close()

