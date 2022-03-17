import sqlite3

class ProcessData:
    
    def __init__(self):
        self.conn = sqlite3.connect("myquotes.db")
        self.curr = self.conn.cursor()
        
    def get_information(self, data: str = '2022-03-17', countr: str = 'Russia', staf: str = '%Tanks%'):
        var = self.curr.execute("""SELECT content
                            FROM quotes_tb
                            WHERE country = ? AND data = ? AND staf LIKE  ?
                          """,
                          (countr, 
                           data,
                           staf
                           ))  
        
        return var.fetchone()[0]   

    def commit_data(self):
        self.conn.commit()
        
        
process_data = ProcessData()
print(process_data.get_information())