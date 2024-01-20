######################### We want to scrap the share of each region in the world population #########################


# Some imports
import urllib
import bs4
import pandas
from urllib import request
import pandas as pd
import re

# We use WIKIPEDIA
URL = 'https://fr.wikipedia.org/wiki/Population_mondiale#%C3%89volution_par_r%C3%A9gion'
request_text = request.urlopen(URL).read()

# GET the html page 
page = bs4.BeautifulSoup(request_text, "lxml")


# Get the sortable table 
table = page.find_all("table", {'class' : 'wikitable sortable'})  


# Get the 'tbody'
table_tbody = table[1].find('tbody')


# Get the 'tr'
table_tr = table_tbody.find_all('tr')

years = []
for element in table_tr[0]:
    if element.text.strip()!= '': 
        years.append(element.text.strip())

data = []
for element in table_tr[1:]:
    if element.text.strip()!= '': 
        sub_list = element.text.strip().split('\n')
        sub_list.pop(1)
        data.append(sub_list)

df = pd.DataFrame(data, columns = years).set_index('Région')
df.to_csv('DATA/share_region_world.csv')
