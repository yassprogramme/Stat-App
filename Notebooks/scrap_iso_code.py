######################### We want to scrap the ISO CODE of all countries in the world #########################


# Some imports
import urllib
import bs4
import pandas
from urllib import request
import pandas as pd
import re

# We use WIKIPEDIA
URL = 'https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes'
request_text = request.urlopen(URL).read()

# GET the html page 
page = bs4.BeautifulSoup(request_text, "lxml")


# Get the sortable table 
table = page.find("table", {'class' : 'wikitable sortable'})  


# Get the 'tbody'
table_tbody = table.find('tbody')


# Get the 'tr'
table_tr = table_tbody.find_all('tr')


# Get the columns
columns = []
for element in table_tr[1].find_all('th'):
    columns.append(element.text.strip())

columns = [col.split('[')[0] for col in columns]
columns = [columns[0]] + [columns[4]]

row = []
# On récupère les informations correspondantes
for i, donnees in enumerate(table_tr):
    if i>1:
        recup = donnees.find_all('td')
        for j, element in enumerate(recup):
            if j==0 or j==4:
                row.append(element.text.strip())

values = [[row[2 * k].replace('\u200a', '').split('[')[0].split('(')[0], row[2 * k + 1]] for k in range(int(len(row) / 2))]

df = pd.DataFrame(values, columns = columns)
df.to_csv('DATA/SCRAP_countries_ISO.csv')