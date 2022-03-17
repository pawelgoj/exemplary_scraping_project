from asyncio.windows_events import NULL
import scrapy
import datetime
from ..items import OryxItem
from ..text_procesing.FindItem import clean_data

def check_country(item):
    pass

def extract_staf_type(item):
    pass

class Oryx(scrapy.Spider):
    name ='oryx'
    start_urls = ['https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html']
    
    def parse(self, response):
        data = datetime.date.today()
        data = data.strftime("%Y-%m-%d")
        items = OryxItem()
        country = 'Unknown'
        
        element = response.css('div[itemprop=articleBody]:nth-last-child(1)')
        for item in element.css('h3'):
            text_1 = item.css('span::text').get()
            text_2 = item.css('h3::text').get()

            if text_2 == "\n":
                pass
            else:
                w = clean_data(text_1, text_2)
                
                if type(w) == type(tuple()):
                    items['data'] = data 
                    items['country'] = country
                    items['staf'] = w[0] 
                    items['content'] = w[1]
                    
                    yield items
                    
                elif w != None:
                    country = w
        
        '''
        Przykład scrapowania za pomocą lików 
        next_page =  response.css('li.next a::attr(href)').get()
        
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            
        Mozna wykonoać też wykorzystac paginację wtedy w linku 
        http://page.com/page/1/
        zwiękaszy umerek na końcu strony w ża załaduje się tyle stron ile nas interesuje 
        
        logowanie się przez scrapy do formularzu 
        -pobieramy token jest na stronie w html
        token = response.css('form input::attr(value)').extract_first()
        -wypełnianie i wysłanie formularza
        return FormRequest.from_response(response, formdata={
            'csrf_token' : token,
            'username' : "username"
            
        }, callback = funkcje_która_skrapować_stronę_po_wypełnieniu_i_wysłaniu_formularza)
        '''