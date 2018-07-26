import os
import datetime
import numpy as np
import pandas as pd
myDir = 'C:\\Users\\blas.leiro\\Documents\\unilever_predictor\\app\\files\\output\\apo_ar_batch_2018-07-09.txt'



df = pd.read_csv(myDir, delimiter='\t', header=None)
df =  df[2]
df.drop_duplicates(inplace=True)
df.to_csv('C:\\Users\\blas.leiro\\Documents\\insulto.csv', index=False)