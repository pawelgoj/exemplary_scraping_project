from __future__ import annotations
import sqlite3
from urllib.request import DataHandler
from pprint import pprint
from pandas import DataFrame
import datetime
import pickle
import logging


class DataToProcesing():
    country = ('Russia', 'Ukraine')
    equipment_type = {
        'Tanks': 'Tanks',
        'Helicopters': 'Helicopters',
        'Naval Ships': 'Naval Ships',
        'Aircraft': 'Aircraft',
        'UAV': 'Unmanned Aerial Vehicles',
        'Artillery': ('Towed Artillery', 'Heavy Mortars', 'Self-Propelled Artillery'),
        'Armoured Personnel Carriers': ('Armoured Personnel Carriers', 'Infantry Mobility Vehicles', 
                                        'Infantry Fighting Vehicles', 'Armoured Fighting Vehicles'),
        'Logistics Trains': 'Logistics Trains',
        'Vehicles': ('Trucks, Vehicles and Jeeps', 'Jammers And Deception Systems', 
                     'Engineering Vehicles', 'Mine-Resistant Ambush Protected'),
        'Radars': 'Radars',
        'Communications Stations': ('Communications Stations', 'Radars And Communications Equipment ', 'Command Posts And Communications Stations'),
        'Rocket Launchers': ('Multiple Rocket Launchers', 'Surface-To-Air Missile Systems', 'Self-Propelled Anti-Tank Missile Systems'),
        'Anti-Aircraft': ('Anti-Aircraft Guns', 'Self-Propelled Anti-Aircraft Guns')
    }
    
class ProcessDataMultiple:
    
    def __init__(self, process_data: ProcessData, data: dict = DataToProcesing.equipment_type, 
                 country: tuple = DataToProcesing.country, date: str = '2022-03-17'):
        self._propcess_data = process_data
        self._data = data
        self._countries = country
        self._date = date
        
    @property
    def date(self):
        return self._countries
    
    @property
    def data(self):
        return self._data
    
    @property
    def country(self):
        return self._countries
    
    @data.setter
    def set_data(self, data):
        self._data = data 
        
    @country.setter
    def set_country(self, country):
        self._countries = country 
        
    @date.setter
    def set_date(self, date: str):
        self._date = date
        
    def to_day(self):
        date = datetime.date.today()
        self._date = date.strftime("%Y-%m-%d")
        
    def process_data(self):
        
        self.resalts = {}
        
        for country in self._countries:
            staf_dict = {}
            for key, items in self._data.items():
                number = 0
                
                if type(items) == type(''):
                    items = items + '%'
                    number = self._propcess_data.get_information(self._date, country, items)
                    
                else:
                    for item in items:
                        item = item + '%'
                        quantity = self._propcess_data.get_information(self._date, country, item)
                        number += quantity
                        
                staf_dict.update({key: number})
                    
            self.resalts.update({country: staf_dict})
            
    def return_resalts(self):
        self.resalts_data_frame = DataFrame.from_dict(self.resalts, orient='columns')
        return self.resalts_data_frame
        

class ProcessData:
    
    def __init__(self):
        
        try:
            with open('name.p', 'rb') as file:
                name = pickle.load(file)
                
        except:
            logging.error('Database dont exist!!!!')
            
        else:
            self.conn = sqlite3.connect(name + ".db")
            self.curr = self.conn.cursor()
        
    def get_information(self, data: str = '2022-03-17', countr: str = 'Russia', staf: str = '%Tanks%'):
        staf = staf + '%'
        var = self.curr.execute("""SELECT content
                            FROM quotes_tb
                            WHERE country = ? AND data = ? AND staf LIKE ? and length(staf) <= length(?) + 1
                          """,
                          (countr, 
                           data,
                           staf,
                           staf
                           ))  
        
        try: 
            resoult = var.fetchone()[0]
        except:
            resoult = 0
            
        return int(resoult)

    def commit_data(self):
        self.conn.commit()
        
class Script:
    def __init__(self, date: str = 'None', to_day: bool = True):
        
        process_data = ProcessData()

        process_data_multiple = ProcessDataMultiple(process_data)
        
        if to_day == True:
            
            process_data_multiple.to_day()
        
        elif to_day == False:
            
            try:
                process_data_multiple.set_date = date
                
            except:
                pass
            
        process_data_multiple.process_data()
        self.output = process_data_multiple.return_resalts()
        pprint(self.output)
        
    def save_data(self, file):
        file = '../' + file + '.csv'
        self.output.to_csv(file)
        

    