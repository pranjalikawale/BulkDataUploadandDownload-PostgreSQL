import psycopg2

conn=psycopg2.connect(database="testdb", user = "postgres", password = "123", host = "127.0.0.1", port = "5432")
print("Opened database successfully")
cur = conn.cursor()
'''
cur.execute("CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME TEXT    NOT NULL,
      AGE  INT     NOT NULL,
      ADDRESS  CHAR(50),
      SALARY   REAL)")
print("Table created successfully")
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) 
      VALUES (1, 'Alex', 32, 'California', 20000.00 ),
             (2, 'Tom', 25, 'Texas', 15000.00 ),
             (3, 'Sheri', 23, 'Norway', 20000.00 ),
             (4, 'Thomas', 25, 'Rich-Mond ', 65000.00 )")
conn.commit()
print("Records created successfully")
cur.execute("CREATE TABLE DEPARTMENTS(
            DEPT_ID INT PRIMARY KEY NOT NULL,
            DEPT CHAR(50) NOT NULL,
            EMP_ID INT NOT NULL
)")
conn.commit()
print("Table created successfully")
cur.execute("INSERT INTO DEPARTMENTS (DEPT_ID, DEPT, EMP_ID)
             VALUES (1, 'IT Billing', 1 ),
             (2, 'Engineering', 2 ),
             (3, 'Finance', 7 )")
conn.commit()
print("Records created successfully")
'''
cur.execute("SELECT * FROM COMPANY WHERE AGE::text LIKE '2%'")
rows = cur.fetchall()
print("\nid\t name\t age\t address\t salary\n")
for row in rows:
   print(f"{row[0]}\t {row[1]}\t {row[2]} \t{row[3]} {row[4]}") 
conn.commit()
print("Operation LIKE done successfully")

cur.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
print("Operation UPDATE done successfully")

cur.execute("DELETE from COMPANY where ID=2")
print("Operation DELETE done successfully")

cur.execute("SELECT * from COMPANY")
rows = cur.fetchall()
print("\nid\t name\t age\t address\t salary\n")
for row in rows:
   print(f"{row[0]}\t {row[1]}\t {row[2]} \t{row[3]} {row[4]}") 
conn.commit()
print("Operation SELECT done successfully")
#cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (5, 'Alex', 32, 'California', 20000.00 )")

cur.execute("SELECT NAME FROM COMPANY GROUP BY NAME HAVING count(NAME) > 1 ORDER BY NAME")
rows = cur.fetchall()
print("\n name\n")
for row in rows:
   print(f" {row[0]}") 
conn.commit()
print("Operation GROUP BY, HAVING and ORDER BY and  done successfully")

# Operation CROSS JOIN
cur.execute("SELECT EMP_ID, NAME, DEPT FROM COMPANY CROSS JOIN DEPARTMENTS")
rows = cur.fetchall()
print("\nEMP_ID\t NAME\t DEPT\n")
for row in rows:
   print(f"{row[0]}\t {row[1]}\t {row[2]}") 
conn.commit()
print("Operation CROSS JOIN done successfully")

# Operation INNER JOIN
cur.execute("SELECT EMP_ID, NAME, DEPT FROM COMPANY INNER JOIN DEPARTMENTS ON COMPANY.ID = DEPARTMENTS.EMP_ID")
rows = cur.fetchall()
print("\nEMP_ID\t NAME\t DEPT\n")
for row in rows:
   print(f"{row[0]}\t {row[1]}\t {row[2]}") 
conn.commit()
print("Operation INNER JOIN done successfully")

# Operation LEFT OUTER JOIN
cur.execute("SELECT EMP_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENTS ON COMPANY.ID = DEPARTMENTS.EMP_ID")
rows = cur.fetchall()
print("\nEMP_ID\t NAME\t DEPT\n")
for row in rows:
   print(f"{row[0]}\t {row[1]}\t {row[2]}") 
conn.commit()
print("Operation LEFT OUTER JOIN done successfully")

# Operation RIGHT OUTER JOIN
cur.execute("SELECT EMP_ID, NAME, DEPT FROM COMPANY RIGHT OUTER JOIN DEPARTMENTS ON COMPANY.ID = DEPARTMENTS.EMP_ID")
rows = cur.fetchall()
print("\nEMP_ID\t NAME\t DEPT\n")
for row in rows:
   print(f"{row[0]}\t {row[1]}\t {row[2]}") 
conn.commit()
print("Operation RIGHT OUTER JOIN done successfully")

# Operation FULL OUTER JOIN
cur.execute("SELECT EMP_ID, NAME, DEPT FROM COMPANY FULL OUTER JOIN DEPARTMENTS ON COMPANY.ID = DEPARTMENTS.EMP_ID")
rows = cur.fetchall()
print("\nEMP_ID\t NAME\t DEPT")
for row in rows:
   print(f"{row[0]}\t {row[1]}\t {row[2]}") 
conn.commit()
print("Operation FULL OUTER JOIN done successfully")
conn.close()
conn.close()
