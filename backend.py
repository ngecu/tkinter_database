#Concurrent with main app
import sqlite3


#Make a connection with the database
def connect():
    conn = sqlite3.connect('source.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dictionary (id INTEGER PRIMARY KEY,word TEXT , photo BLOB ,definition TEXT )")
    conn.commit()
    conn.close()



def view():
    conn=sqlite3.connect("source.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM dictionary")
    rows=cur.fetchall()
    conn.close()
    return rows
    
    

    

def search(word,photo="", definition=""):
    conn = sqlite3.connect('source.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM dictionary WHERE word = ? OR photo=? OR definition=?",(word,photo,definition))
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('source.db')
    cur = conn.cursor()
    cur.execute("DELETE  FROM dictionary WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,word,photo,definition):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE dictionary SET word=?, photo=? definition=? WHERE id =?",(word,photo,definition,id))
    conn.commit()
    conn.close()

connect()


