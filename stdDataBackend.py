import sqlite3
#backend
def studentData():
    con=sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (ID INTEGER PRIMARY KEY, stdID TEXT, Firstname TEXT, Lastname TEXT, DoB TEXT,\
     Age TEXT, Gender TEXT, Address TEXT, Mobile TEXT)")
    con.commit()
    con.close()

def AddStdRec(stdID, Firstname, Lastname, DoB, Age, Gender, Address, Mobile):
    con=sqlite3.connect("student.db")
    cur =con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (stdID, Firstname, Lastname, DoB, Age,
                Gender, Address, Mobile))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows =cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(stdID="", Firstname="", Lastname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE stdID=? OR Firstname=? OR Lastname=? OR DoB=? OR Age=? OR Gender=? OR Address=? \
     OR Mobile=?", (stdID, Firstname, Lastname, DoB, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    con.close()
    return rows

def Update(id,stdID="", Firstname="", Lastname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET stdID=? OR Firstname=? OR Lastname=? OR DoB=? OR Age=? OR Gender=? OR Address=? \
         OR Mobile=?", (stdID, Firstname, Lastname, DoB, Age, Gender, Address, Mobile, id))
    con.commit()
    con.close()
    return


studentData()