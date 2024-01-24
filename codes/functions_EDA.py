import matplotlib.pyplot as plt
import seaborn as sns 

def get_migrants(dataframe, start, destination): 
    """ 
    dataframe : dataframe considered 
    start : origin
    destination : where the migrant goes
    Function that displays the distribution (pie) of migrants' main destinations (8) for a given country. 
    """
    return dataframe.iloc[start,destination]

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


def total_migration(dataframe):
    return print("Destination of migrants \n", "\n", dataframe.sum(), "\n", "\n", 
                 "\nThere is", dataframe.sum().sum(), "migrations in total")

def get_trend(dataframe):
    """ 
    dataframe : dataframe considered 
    Function which gets the trend of migration flows for a given period. 
    """
    dataframe = dataframe / dataframe.sum().sum()  #we first regularized our dataset 
    stacked_series = dataframe.stack()
    top_values = stacked_series.nlargest(5)
    values = top_values.values
    top_indices = top_values.index
    top_rows = [index[0] for index in top_indices]
    top_columns = [index[1] for index in top_indices]
    return print("The 5 main population movements (based on regularized data) concern migrants moving from :\n",
                 top_rows[0], "to", top_columns[0], f"representing {values[0] * 100}% of total migrations \n",
                 top_rows[1], "to", top_columns[1], f"representing {values[1] * 100}% of total migrations \n",
                 top_rows[2], "to", top_columns[2], f"representing {values[2] * 100}% of total migrations \n",
                 top_rows[3], "to", top_columns[3], f"representing {values[3] * 100}% of total migrations \n",
                 top_rows[4], "to", top_columns[4], f"representing {values[4] * 100}% of total migrations \n")

def obtenir_tendance(dataframe):
    """ 
    dataframe : dataframe considered 
    Function which gets the trend of migration flows for a given period. 
    """
    dataframe = dataframe / dataframe.sum().sum()  #we first regularized our dataset 
    stacked_series = dataframe.stack()
    top_values = stacked_series.nlargest(5)
    values = top_values.values
    top_indices = top_values.index
    top_rows = [index[0] for index in top_indices]
    top_columns = [index[1] for index in top_indices]
    return print("Les 5 principaux mouvements de population (sur des données régularisées) concernent les migrants partant de :\n",
                 top_rows[0], "to", top_columns[0], f"Représentant {values[0] * 100}% du total des migrations  \n",
                 top_rows[1], "to", top_columns[1], f"Représentant {values[1] * 100}% du total des migrations  \n",
                 top_rows[2], "to", top_columns[2], f"Représentant {values[2] * 100}% du total des migrations  \n",
                 top_rows[3], "to", top_columns[3], f"Représentant {values[3] * 100}% du total des migrations  \n",
                 top_rows[4], "to", top_columns[4], f"Représentant {values[4] * 100}% du total des migrations  \n")
