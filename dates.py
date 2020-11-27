import pandas as pd
import datetime

array_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

date = pd.to_datetime(dataset['DATA_CONFIRMACAO'], format='%d/%m/%Y', utc=True);

dataset['newCol_date'] = date.apply(lambda x: x.strftime('%Y-%m-%d'));
dataset['newCol_mes'] = date.dt.month.apply(lambda x: array_meses[x - 1]);
dataset['newCol_ano'] = date.dt.year

dataset
    