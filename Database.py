import sqlite3

class Database():
    def __init__(self):
        self.db = sqlite3.connect('database.db')
        self.cursor = self.db.cursor()

    def newUser(self,name1,age1,height1,weight1,gender1):
        self.cursor.execute('''INSERT INTO person(name,age,height,weight,gender)
                          VALUES(?,?,?,?,?)''', (name1,age1,height1,weight1,gender1,))
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

    def check(self,name1):
        self.cursor.execute('''SELECT id FROM person WHERE name = ?''', (name1,))
        if self.cursor.fetchone() is None:
            return False
        else:
            return True

    def close(self):
        self.db.close()
