import pandas as pd
import os

path = "C:\\Users\\brunn\\Desktop\\SENAC\\topicos-avancados"
files = os.listdir(path)

extension = 'csv'
files_open = [path + '\\' + f for f in files if f[-len(extension):] == extension]

list_of_dataframes = []

for file in files_open:
  list_of_dataframes.append(pd.read_csv(file, delimiter=';'))
  
merged_data = pd.concat(list_of_dataframes)

merged_data