import sqlite3

conn = sqlite3.connect('company.db')
print("successfully connected to the database")

conn.execute("UPDATE COMPANY2 set SALARY=45000.00 where ID=1")
conn.commit()

data = conn.execute("SELECT * FROM COMPANY2")
for rows in data:
    print("ID:",rows[0])
    print("FIRSTNAME:",rows[1])
    print("LASTNAME:",rows[2])
    print("AGE:",rows[3])
    print("SALARY:",rows[4])
    print("TASK:",rows[5])
conn.close()