import psycopg2

conn=psycopg2.connect(database="testdb", user = "postgres", password = "123")
print("Opened database successfully")
cur = conn.cursor()

cur.execute('''
                CREATE table Batsman(sr_no int PRIMARY KEY NOT NULL, 
                                    player varchar(40) NOT NULL )
            ''')

# upload data     
with open('C:\\Users\\User\\Desktop\\python\\Postgress_DB\\baller.csv', 'r') as file_input:
    next(file_input) # Skip the header row.
    cur.copy_from(file_input, 'Batsman', sep=',')

# Operation Display
cur.execute("SELECT * FROM Batsman")
rows = cur.fetchall()
print("\nSr_No\t NAME")
for row in rows:
   print(f"{row[0]}\t {row[1]}") 

# Use the COPY function on the SQL we created above.
SQL_for_file_output = "COPY ({0}) TO STDOUT WITH CSV HEADER".format("SELECT * FROM Batsman")

#download data
with open('C:\\Users\\User\\Desktop\\python\\Postgress_DB\\batsman.csv', 'w') as file_output:
    cur.copy_expert(SQL_for_file_output, file_output)

cur.execute("TRUNCATE TABLE Batsman")
cur.execute("DROP TABLE Batsman")
conn.commit()
print("Operation of Upload and download done successfully")
cur.close()
conn.close()