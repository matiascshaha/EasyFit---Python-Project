import sqlite3

db = sqlite3.connect('database.db')
db.execute('''CREATE TABLE person (id INTEGER PRIMARY KEY, name TEXT,
              height INTEGER, weight INTEGER, gender TEXT)''')

db.close()
