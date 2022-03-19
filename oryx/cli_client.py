import click
from process_data import Script
import logging
import os
from create_delete_data_base import Data_base

@click.command()
@click.argument('process_type', nargs=1)
@click.option('--date', default='to_day', help='data from date: yyyy-mm-dd')
@click.option('--name', default='data_base', help='data base name')
@click.option('--file', default='', help='file name for data processing')
def make_scraping(process_type, date, name, file):
    """process_type: scraping, data_processing, create_database, drop_database"""
    
    if process_type == 'data_processing':
        
        if date == 'to_day':
            script = Script()
            
        else:
            script = Script(date, to_day=False)
            
        if file != '':
            script.save_data(file)
            
            
    elif process_type == 'scraping':
        
        logging.info("scraping!!!!")
        #execute cli comand 
        os.system("scrapy crawl oryx")
        
        
    elif process_type == 'create_database':
        data_base = Data_base(name)
        data_base.create_database()
        
    elif process_type == 'drop_database':
        data_base = Data_base()
        data_base.drop_database()
        
    else:
        logging.error("Wrong process type. process_type: scraping," 
                      "data_processing, create_database, drop_database")
    
    
if __name__ == '__main__':
    make_scraping()