import logging
import sqlite3
import logging
import pickle
import os

class Data_base():
    def __init__(self, name: str = 'name'):
        self._name = name
        
    def create_connection(self):
        self.conn = sqlite3.connect(self._name + ".db")
        self.curr = self.conn.cursor()
        
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        self.curr.execute("""create table quotes_tb(
            data text,
            country text,
            staf text,
            content text
            )""")
        
    def commit_data(self):
        self.conn.commit()
        self.conn.close()

    def create_database(self):
        self.create_connection()
        self.create_table()
        self.commit_data()
        with open('name.p', 'wb') as file:
            pickle.dump(self._name, file)
        
    def drop_database(self):
        
        try:
            with open('name.p', 'rb') as file:
                name = pickle.load(file)
            name = name + '.db'
            print(name)
            os.remove(name)
            os.remove('name.p')
        except: 
            logging.error("Database not exist")