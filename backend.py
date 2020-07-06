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
        cursor.execute(" INSERT INTO dictionary (word, photo, definition) VALUES (?, ?, ?, ?)", ( word, empPhoto, definition))
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("the sqlite connection is closed")


# def insert(word,photo,definition):
#     conn = sqlite3.connect('source.db')
#     cur = conn.cursor()
#     cur.execute("INSERT INTO dictionary VALUES (NULL,?,?,?)",(word,photo,definition))
#     conn.commit()
#     conn.close()

def view():
    conn = sqlite3.connect('source.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM dictionary")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(word):
    conn = sqlite3.connect('source.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM dictionary WHERE word = ?",(word))
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('lite.db')
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
# update(11,6,"Maziwa")

insert("Rain", "ngecu.jpg", "The condensed moisture of the atmosphere falling visibly in separate drops.")

print(view())

