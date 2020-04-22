import sqlite3

class Database():
    def __init__(self):
        self.db = sqlite3.connect('database.db')
        self.cursor = self.db.cursor()

    def newUser(self,name1,height1,weight1,gender1):
        self.cursor.execute('''INSERT INTO person(name,height,weight,gender)
                          VALUES(?,?,?,?)''', (name1,height1,weight1,gender1,))
        self.db.commit()

    def deleteUser(self,name1):
        self.cursor.execute('''DELETE FROM person WHERE name = ?''', (name1,))
        self.db.commit()

    def update(self,name1,weight1):
        self.cursor.execute('''SELECT weight FROM person WHERE name = ?''', (name1,))
        oldWeight = self.cursor.fetchone()
        weightChange = weight1 - oldWeight[0]
        #Positive change = gained ; Negative change = lost
        self.cursor.execute('''UPDATE person SET weight = ? WHERE name = ?''' ,
                          (weight1,name1,))
        self.db.commit()
        return weightChange

    def close(self):
        self.db.close()
