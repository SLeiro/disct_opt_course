import os
import datetime
import numpy as np
import pandas as pd
myDir = os.getcwd()



df = pd.read_csv(os.path.join(myDir,'Input','pepe.csv'), index_col=0)
df = df[df['pais'] == 'ARGENTINA']
df = df[df['categoria'] == 'TOTAL ONE']
lista = df.columns
i = 0
columns = []
for column in lista:
    columns.append(column)
    i += 1
print(columns)
dataframe = pd.pivot_table(df, index=['alerta '], columns=['fecha'], values=['valor'], aggfunc=np.sum)
# print(dataframe)
# print(df)