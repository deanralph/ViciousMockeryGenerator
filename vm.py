import sqlite3

def resetUsed(dbName):
    with sqlite3.connect(dbName) as resetConn:
        resetCur = resetConn.cursor()
        resetCur.execute("UPDATE Mockery SET Used = 0")
        resetConn.commit()

def addInsult(dbName, newInsult):
    with sqlite3.connect(dbName) as addConn:
        addCur = addConn.cursor()
        addCur.execute(f"INSERT INTO Mockery (Insult, Used) VALUES ('{newInsult}', 0)")
        addConn.commit()

def deleteInsult(dbName, newInsult):
    with sqlite3.connect(dbName) as addConn:
        addCur = addConn.cursor()
        addCur.execute(f"DELETE FROM Mockery WHERE Insult = '{newInsult}'")
        addConn.commit()

def getInsult(dbName):
    conn = sqlite3.connect(dbName)
    sql = "select Insult from Mockery where Used = 0 ORDER BY RANDOM() LIMIT 1"
    cur = conn.cursor()
    cur.execute(sql)
    insult = cur.fetchone()
    print(insult[0])
    updatesql = f"UPDATE Mockery SET Used = 1 where Insult = '{insult[0]}'"
    cur.execute(updatesql)
    conn.commit()
    conn.close()

# resetUsed("vm.db")
for x in range(30):
    getInsult("vm.db")