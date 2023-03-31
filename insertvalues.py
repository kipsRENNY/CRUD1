import sqlite3
conn = sqlite3.connect("company.db")
print("connected")

conn.execute("INSERT INTO Company2(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
VALUES(1,'John','Allan',21,30000,'Manager')");
conn.execute("INSERT INTO Company2(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
VALUES(2,'Andrew','Koech',21,25000,'Ass Manager')");
conn.execute("INSERT INTO Company2(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
VALUES(3,'faith','Achieng',21,15000,'trainer')");
conn.execute("INSERT INTO Company2(ID,FIRSTNAME,LASTNAME,AGE,SALARY,TASK)\
VALUES(4,'clara','Wanjiru',21,10000,'secretary')");
conn.commit()

print("Successfully inserted values")

conn.close()