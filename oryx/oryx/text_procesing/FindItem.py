import re 


def clean_data(item1, item2):
    if None == item1 and item2 != None:
        matching = re.search(r"^[a-zA-Z\-\ ()]+", item2)
        item1 = matching.group(0)
        item2 = item2[matching.end():]
        if item1[-2:] == ' (':
            item1 = item1[:-2]
            
        item2 = find_number_of_items(item2)
        
        return item1, item2
    
    elif item2 == None and item1 != None:
        country = find_country(item1)
        
        return country
    
    elif None != item1 and item2 != None:
        item2 = find_number_of_items(item2)
        
        return item1, item2
    
def find_country(item1):
    country = 'Unknown'
    if 'Russia' in item1:
        country = 'Russia'
    elif 'Ukraine' in item1:
        country = 'Ukraine'
        
    return country

def find_number_of_items(item2):
    matching = re.search(r"([0-9]+)", item2)
    item2 = matching.group(0)
    
    return item2

 

