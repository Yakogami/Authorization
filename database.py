import sqlite3


class Database:
    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file)
        proxy = self.connection.cursor()
        proxy.execute("""CREATE TABLE IF NOT EXISTS Users_database 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, Login TEXT NOT NULL, Password TEXT NOT NULL, Registration_Date TEXT NOT NULL)""")
        self.connection.commit()

    def insert(self, username, password, registration_date):
        proxy = self.connection.cursor()
        proxy.execute('INSERT INTO Users_database (Login, Password, Registration_Date) VALUES (?,?, ?)', (username, password, registration_date))
        self.connection.commit()

    # def delete_all_history(self):
    #     proxy = self.connection.cursor()
    #     proxy.execute('DELETE FROM History')
    #     self.connection.commit()
    #
    # def get_history(self):
    #     proxy = self.connection.cursor()
    #     proxy.execute('SELECT * FROM History')
    #     return proxy.fetchall()
    #
    # def get_winrate(self):
    #     proxy = self.connection.cursor()
    #     proxy.execute('SELECT SUM(CASE WHEN Result="Win" THEN 1 ELSE 0 END), COUNT(Result) FROM History ')
    #     return proxy.fetchall()[0]
