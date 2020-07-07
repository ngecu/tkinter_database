import sqlite3

def connect():
    conn = sqlite3.connect('source.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dictionary (id INTEGER PRIMARY KEY,word TEXT , photo BLOB ,definition TEXT )")
    conn.commit()
    conn.close()

def convertToBinaryData(filename):
    #Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insert(word, photo, definition):
    try:
        sqliteConnection = sqlite3.connect('source.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        empPhoto = convertToBinaryData(photo)
        # Convert data into tuple format
        cursor.execute(" INSERT INTO dictionary (word, photo, definition) VALUES (?, ?, ?)", ( word, empPhoto, definition))
        with open ('static/{}.png'.format(word),'wb') as f:
            f.write(empPhoto)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")

def view():
    conn=sqlite3.connect("source.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM dictionary")
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn=sqlite3.connect("source.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM dictionary WHERE id=?",(id,))
    print("deleted")
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("source.db")
    cur=conn.cursor()
    cur.execute("UPDATE dictionary SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()
