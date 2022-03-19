# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
import pickle

class OryxPipeline:
    def __init__(self):
        with open('name.p', 'rb') as file:
            self.name = pickle.load(file)
        self.create_connection() 
    
    def create_connection(self):
        self.conn = sqlite3.connect(self.name + ".db")
        self.curr = self.conn.cursor()
    
    def process_item(self, item, spider):
        self.store_db(item)

        return item

    def store_db(self, item):
        self.curr.execute("""insert into quotes_tb values (?,?,?,?)""", (
            item['data'],
            item['country'],
            item['staf'],
            item['content']
        ))
        
        self.conn.commit()