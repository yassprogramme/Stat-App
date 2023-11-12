import matplotlib.pyplot as plt
import seaborn as sns 

def destination_migrants(dataframe, start):
    """ 
    dataframe : dataframe considered 
    start : origin
    Function that displays the distribution (pie) of migrants' main destinations (8) for a given country. 
    """
    data = dataframe.loc[start].sort_values(ascending = False)[0:7]
    plt.figure(figsize=(6, 6))  
    sns.set_style("whitegrid")
    plt.pie(data, labels = data.index, autopct='%1.1f%%', startangle=90)
    plt.title(f'Destination of migrants from {start}') 
    plt.show()
    return None


def destination_migrants_top5(dataframe, start):
    """ 
    dataframe : dataframe considered 
    start : origin
    Function that displays the distribution of migrants' main destinations (5) for a given country. 
    """
    data = dataframe.loc[start].sort_values(ascending = False)[0:5]
    plt.plot(data, kind='area', 
             stacked=False,
             figsize=(10, 8), 
             )
    plt.title(f'Top 5 destination of migrants from {start}') 
    plt.show()
    return None
