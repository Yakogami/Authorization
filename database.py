import sqlite3
from hashlib import sha256


class Database:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        proxy = self.connection.cursor()
        proxy.execute("""CREATE TABLE IF NOT EXISTS Users_database 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, Login TEXT UNIQUE NOT NULL, Password TEXT NOT NULL)""")
        self.connection.commit()

    def insert_users(self, username, password):
        proxy = self.connection.cursor()
        proxy.execute('INSERT INTO Users_database (login, password) VALUES (?,?)',
                      (username, sha256(password.encode()).hexdigest()))
        self.connection.commit()

    def get_users(self):
        proxy = self.connection.cursor()
        proxy.execute('SELECT Login FROM Users_database ')
        return proxy.fetchall()

    def auth_user(self, username, password):
        proxy = self.connection.cursor()
        proxy.execute('SELECT Login FROM Users_database WHERE login=? AND password=?',
                      (username, sha256(password.encode()).hexdigest()))
        result = proxy.fetchall()

    def all_users(self):
        proxy = self.connection.cursor()
        proxy.execute('SELECT * FROM Users_database ')
        return proxy.fetchall()
