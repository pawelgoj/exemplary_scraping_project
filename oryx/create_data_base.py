import sqlite3

class Data:
    def __init__(self):
        pass
    def create_connection(self):
        self.conn = sqlite3.connect("myquotes.db")
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

data = Data()
data.create_connection()
data.create_table()
data.commit_data()
