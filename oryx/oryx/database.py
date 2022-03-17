import sqlite3

conn = sqlite3.connect('myquotes.db')

corr = conn.cursor()

''' corr.execute("""create table quotes_tb(
            staf text,
            content text
            )""")
 '''
 
corr.execute("""insert into quotes_tb values ('test', 'test')""")
conn.commit()
conn.close()