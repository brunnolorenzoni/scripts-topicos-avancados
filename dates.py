import pandas as pd
import datetime

array_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

dateFormated = pd.to_datetime(dataset['DATA_CONFIRMACAO'], format='%d/%m/%Y');

dataset['newCol_date'] = dateFormated
dataset['newCol_mes'] = dateFormated.dt.month
dataset['newCol_ano'] = dateFormated.dt.year

dataset