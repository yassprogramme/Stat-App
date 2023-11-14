import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import os
from functools import reduce

os.chdir('/Users/augustincablant/Documents/GitHub/Stat-App')
df1 = pd.read_excel('DATA/dataset1.xlsx', sheet_name = "flow estimates by region 2005")
df2_90_95 = pd.read_excel('DATA/dataset2.xlsx', sheet_name= '1990-95')
df2_95_00 = pd.read_excel('DATA/dataset2.xlsx', sheet_name= '1995-2000')
df2_2000_05 = pd.read_excel('DATA/dataset2.xlsx', sheet_name= '2000-05')
df2_2005_10 = pd.read_excel('DATA/dataset2.xlsx', sheet_name= '2005-10')

# First dataset
def clean1(dataframe):
    columns = ['/', 'North America', 'Central America', 'South America', 'North Africa', 'Sub-Saharan Africa', 'Northern Europe', 'Western Europe', 
               'Southern Europe', 'Eastern Europe', 'Central Asia', 'Western Asia', 'South Asia', 'East Asia', 'South-East Asia', 'Oceania']
    dataframe.drop('Unnamed: 0', axis = 1, inplace = True)
    dataframe.columns = columns 
    return dataframe[1:]
dataset1 = clean1(df1)
dataset1.to_csv('DATA/dataset1.csv')


# Second dataset 
# Get the iso code
iso = ['ABW', 'AFG', 'AGO', 'ALB', 'ARE', 'ARG', 'ARM', 'AUS', 'AUT', 'AZE', 'BDI', 'BEL', 'BEN', 'BFA', 'BGD', 'BGR',
        'BHR', 'BHS', 'BIH', 'BLR', 'BLZ', 'BOL', 'BRA', 'BRB', 'BRN','BTN', 'BWA', 'CAF', 'CAN', 'CHE', 'CHI', 'CHL', 'CHN', 'CIV',
        'CMR', 'COD', 'COG', 'COL', 'COM', 'CPV', 'CRI', 'CUB', 'CYP', 'CZE', 'DEU', 'DJI', 'DNK', 'DOM', 'DZA', 'ECU', 'EGY', 'ERI', 
        'ESH', 'ESP', 'EST', 'ETH', 'FIN', 'FJI', 'FRA', 'FSM', 'GAB', 'GBR', 'GEO', 'GHA', 'GIN', 'GLP', 'GMB', 'GNB', 'GNQ', 'GRC',
        'GRD', 'GTM', 'GUF', 'GUM', 'GUY', 'HKG', 'HND', 'HRV', 'HTI', 'HUN', 'IDN', 'IND', 'IRL', 'IRN', 'IRQ', 'ISL', 'ISR', 'ITA',
        'JAM', 'JOR', 'JPN', 'KAZ', 'KEN', 'KGZ', 'KHM', 'KOR', 'KWT', 'LAO', 'LBN', 'LBR', 'LBY', 'LCA', 'LKA', 'LSO', 'LTU', 'LUX',
        'LVA', 'MAC', 'MAR', 'MDA', 'MDG', 'MDV', 'MEX', 'MKD', 'MLI', 'MLT', 'MMR', 'MNE', 'MNG', 'MOZ', 'MRT', 'MTQ', 'MUS', 'MWI',
        'MYS', 'MYT', 'NAM', 'NCL', 'NER', 'NGA', 'NIC', 'NLD', 'NOR', 'NPL', 'NZL', 'OMN', 'PAK', 'PAN', 'PER', 'PHL', 'PNG', 'POL',
        'PRI', 'PRK', 'PRT', 'PRY', 'PSE', 'PYF', 'QAT', 'REU', 'ROU', 'RUS', 'RWA', 'SAU', 'SDN', 'SEN', 'SGP', 'SLB', 'SLE', 'SLV',
        'SOM', 'SRB', 'SSD', 'STP', 'SUR', 'SVK', 'SVN', 'SWE', 'SWZ', 'SYR', 'TCD', 'TGO', 'THA', 'TJK', 'TKM', 'TLS', 'TON', 'TTO',
        'TUN', 'TUR', 'TZA', 'UGA', 'UKR', 'URY', 'USA', 'UZB', 'VCT', 'VEN', 'VIR', 'VNM', 'VUT', 'WSM', 'YEM', 'ZAF', 'ZMB', 'ZWE']

# Name of the countires 
countries = ['Aruba', 'Afghanistan', 'Angola', 'Albania',
        'United Arab Emirates', 'Argentina', 'Armenia', 'Australia',
        'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin',
        'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas',
        'Bosnia and Herzegovina', 'Belarus', 'Belize', 'Bolivia',
        'Brazil', 'Barbados', 'Brunei', 'Bhutan', 'Botswana',
        'Central African Republic', 'Canada', 'Switzerland',
        'Channel Islands', 'Chile', 'China', 'Ivory Coast', 'Cameroon',
        'Democratic Republic of the Congo', 'Republic of Congo',
        'Colombia', 'Comoros', 'Cape Verde', 'Costa Rica', 'Cuba',
        'Cyprus', 'Czech Republic', 'Germany', 'Djibouti', 'Denmark',
        'Dominican Republic', 'Algeria', 'Ecuador', 'Egypt', 'Eritrea',
        'Western Sahara', 'Spain', 'Estonia', 'Ethiopia', 'Finland',
        'Fiji', 'France', 'Micronesia', 'Gabon', 'United Kingdom',
        'Georgia', 'Ghana', 'Guinea', 'Guadeloupe', 'Gambia',
        'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada',
        'Guatemala', 'French Guiana', 'Guam', 'Guyana', 'Hong Kong',
        'Honduras', 'Croatia', 'Haiti', 'Hungary', 'Indonesia', 'India',
        'Ireland', 'Iran', 'Iraq', 'Iceland', 'Israel', 'Italy',
        'Jamaica', 'Jordan', 'Japan', 'Kazakhstan', 'Kenya',
        'Kyrgyzstan', 'Cambodia', 'South Korea', 'Kuwait', 'Laos',
        'Lebanon', 'Liberia', 'Libya', 'Saint Lucia', 'Sri Lanka',
        'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao',
        'Morocco', 'Moldova', 'Madagascar', 'Maldives', 'Mexico',
        'Macedonia', 'Mali', 'Malta', 'Myanmar', 'Montenegro',
        'Mongolia', 'Mozambique', 'Mauritania', 'Martinique',
        'Mauritius', 'Malawi', 'Malaysia', 'Mayotte', 'Namibia',
        'New Caledonia', 'Niger', 'Nigeria', 'Nicaragua', 'Netherlands',
        'Norway', 'Nepal', 'New Zealand', 'Oman', 'Pakistan', 'Panama',
        'Peru', 'Philippines', 'Papua New Guinea', 'Poland',
        'Puerto Rico', 'North Korea', 'Portugal', 'Paraguay',
        'Palestine', 'French Polynesia', 'Qatar', 'Reunion', 'Romania',
        'Russia', 'Rwanda', 'Saudi Arabia', 'Sudan', 'Senegal',
        'Singapore', 'Solomon Islands', 'Sierra Leone', 'El Salvador',
        'Somalia', 'Serbia', 'South Sudan', 'Sao Tome and Principe',
        'Suriname', 'Slovakia', 'Slovenia', 'Sweden', 'Swaziland',
        'Syria', 'Chad', 'Togo', 'Thailand', 'Tajikistan',
        'Turkmenistan', 'East Timor', 'Tonga', 'Trinidad and Tobago',
        'Tunisia', 'Turkey', 'Tanzania', 'Uganda', 'Ukraine', 'Uruguay',
        'United States', 'Uzbekistan',
        'Saint Vincent and the Grenadines', 'Venezuela',
        'Virgin Islands', 'Vietnam', 'Vanuatu', 'Samoa', 'Yemen',
        'South Africa', 'Zambia', 'Zimbabwe']

dico = dict(zip(iso, countries))

def clean2(dataframe): 
    period = list(dataframe.columns)[1]
    columns = [period] + iso + ['TOTAL']
    dataframe.drop(['Unnamed: 0',period], axis = 1, inplace = True)
    dataframe.columns = columns
    return dataframe[2:]

df2_90_95 = clean2(df2_90_95)
df2_95_00 = clean2(df2_95_00)
df2_2000_05 = clean2(df2_2000_05)
df2_2005_10 = clean2(df2_2005_10)

# Create a unique dataset
def clean_col(df):
    df.drop('Unnamed: 0', axis = 1, inplace = True)
    col = list(df.columns)[0]
    df.rename({f'{col}':'countries'}, axis = 1, inplace = True)
    df.set_index('countries', inplace = True)
    return df

df2_90_95 = clean_col(df2_90_95)
df2_95_00 = clean_col(df2_95_00)
df2_2000_05 = clean_col(df2_2000_05)
df2_2005_10 = clean_col(df2_2005_10)
df2 = df2_90_95 + df2_95_00 + df2_2000_05 + df2_2005_10

df2.to_csv('DATA/dataset2.csv')
df2_90_95.to_csv('DATA/dataset2_90_95.csv')
df2_95_00.to_csv('DATA/dataset2_95_00.csv')
df2_2000_05.to_csv('DATA/dataset2_00_05.csv')
df2_2005_10.to_csv('DATA/dataset2_05_10.csv')