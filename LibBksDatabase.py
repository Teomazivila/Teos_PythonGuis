import sqlite3


def ConnectData():
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS libbooks (ID INTEGER PRIMARY KEY, MTy TEXT, Ref TEXT, Tit TEXT, Fna TEXT, Lna TEXT,\
         Adr1 TEXT, Adr2 TEXT, pcd TEXT, MNo TEXT, BKID TEXT, Bkt TEXT, Atr TEXT, DBo TEXT, Ddu TEXT, SPr TEXT, LrF TEXT, DoD TEXT, DonL)")
    con.commit()
    con.close()


def addDataRec(Mty, Ref, Tit, Fna, Lna, Adr1, Adr2, pcd, MNo, BKID, Bkt, Atr, DBo, Ddu, SPr, LrF, DoD, DonL):
    con = sqlite3.connect("libbooks.db")
    cur = con.cursor()
    cur.execute("INSERT INTO libbooks VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?,?,)",
                (Mty, Ref, Tit, Fna, Lna, Adr1, Adr2, pcd, MNo, BKID, Bkt, Atr, DBo, Ddu, SPr, LrF, DoD, DonL))
    con.commit()
    con.close()


ConnectData()
