import matplotlib.pyplot as plt
import seaborn as sns 

def destination_migrants(dataframe, start):
    """ 
    dataframe : dataframe considered 
    start : origin
    Function that displays the distribution of migrants' main destinations for a given country. 
    """
    data = dataframe.loc[start].sort_values(ascending = False)[0:7]
    plt.figure(figsize=(6, 6))  
    sns.set_style("whitegrid")
    plt.pie(data, labels = data.index, autopct='%1.1f%%', startangle=90)
    plt.title(f'Destination of migrants from {start}') 
    plt.show()
