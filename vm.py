import sqlite3
import random

conn = sqlite3.connect("vm.db")

#sql = "CREATE TABLE Mockery (Insult VARCHAR(1000), Used INT);"
sql = "select Insult from Mockery where Used = 0"
cur = conn.cursor()
cur.execute(sql)

insultlist = cur.fetchall()
insult = insultlist[random.randint(1, len(insultlist))]

print(insult[0])

updatesql = f"UPDATE Mockery SET Used = 1 where Insult = '{insult[0]}'"

cur.execute(updatesql)
conn.commit()
conn.close()