import os 
import pandas as pd 
import numpy as np 
os.chdir('/Users/augustincablant/Documents/GitHub/Stat-App')

############### We want to recreate regions based on countries dataset ###############
df_correspondance = pd.read_csv('DATA/region_countries.csv')

def country_give_region(iso):
    """ 
    From an iso code gives the regions corresponding
    """
    return df_correspondance[df_correspondance['iso']==iso]['world region'].to_list()[0]

def region_give_list_iso(region):
    """ 
    From a region gives a list of iso code
    """
    iso_list = []
    for iso_code in df_correspondance['iso'].to_list():
        if country_give_region(iso_code).strip() == region.strip():
            iso_list.append(iso_code)
    return iso_list

def create_regions(dataframe):
    """ 
    From a dataframe (list of countries with migration flows) gives a dataframe with regions
    """
    regions = list(df_correspondance['world region'].unique())
    dataframe_region = pd.DataFrame(index = regions, columns = regions)  #create the new dataframe
    dataframe_region = dataframe_region.fillna(0)
    for start_region in list(dataframe_region.index):
        start_countries = region_give_list_iso(start_region)
        for start in start_countries:
            for col in list(dataframe.columns):
                region_end = country_give_region(col)
                flow = dataframe.loc[start, col]
                dataframe_region.loc[start_region, region_end] += flow
    return None






