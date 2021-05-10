import sqlite3 as sql


class TransactionObject(): # INTERAÇÃO COM O BANCO DE DADOS
    database = "Cofres.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, parms=None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return True

    def fetchall(selfself):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False


def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS cofres (id INTEGER PRIMARY KEY , rr TEXT , rc TEXT , idc TEXT , ids TEXT , dt TEXT , lc TEXT)")
    trans.persist()
    trans.disconnect()


initDB()


# MÉTODOS DO CRUD COM O BANCO DE DADOS
def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM cofres")
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def insert(rr, rc, idc, ids, dt, lc):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO cofres VALUES(NULL, ?, ?, ?, ?, ?, ?)", (rr, rc, idc, ids, dt, lc))
    trans.persist()
    trans.disconnect()


def search(rr="", rc="", idc="", ids="", dt="", lc=""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM cofres WHERE rr=? or rc=? or idc=? or ids=? or dt=? or lc=?", (rr, rc, idc, ids, dt, lc))
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def update(id, rr, rc, idc, ids, dt, lc):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE cofres SET rr=?, rc=?, idc=?, ids=?, dt=?, lc=? WHERE id=?", (rr, rc, idc, ids, dt, lc, id))
    trans.persist()
    trans.disconnect()


def delete(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM cofres WHERE id=?", (id,))
    trans.persist()
    trans.disconnect()