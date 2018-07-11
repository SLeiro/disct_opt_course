#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import os
import datetime as dt
from dao import Dao
# myDir = 'C:\\Queries\\Lindt BR\\Procesado'
myDir = 'C:\\Users\\blas.leiro\\Desktop\\Lindt BR\\Cliente_Validacion de data\\Forecast\\2016'

output_dir = 'C:\\Users\\blas.leiro\\Desktop\\Lindt BR\\Cliente_Validacion de data\\Forecast\\CSVS\\'

#
# for root, dirs, files in os.walk(myDir):
#     for forecast_file in files:
#         if 'v4_ajustemaio' in forecast_file and '.csv' in forecast_file:
#             print(forecast_file)
            # df = pd.read_excel(os.path.join(myDir, forecast_file),sheetname='Corrected FCST in CU',
            #                    skiprows=9)
            # df = df[df['act / corrected']=='Corrected']
            # print(df)
            # df.to_csv(os.path.join(myDir, forecast_file+'.csv'), index=False, encoding='utf-8')
            # df = pd.read_csv(os.path.join(myDir, forecast_file), encoding='utf-8')
            # date_list = df.columns.tolist()
            # date_list.remove('Next Soft')
            # df = pd.melt(df, id_vars='Next Soft', value_vars=date_list)
            # df_dates = df['variable'].drop_duplicates().values
            # min_date = dt.datetime.strptime(df_dates[0].split()[0], '%m/%d/%Y')
            # min_date_1 = min_date - dt.timedelta(days=1)
            # min_date_posta =  min_date_1.replace(day=1)
            # print(min_date_posta)
            # df['mes0'] = min_date_posta
            # print(df)
            # df.to_csv(os.path.join(output_dir, forecast_file), index=False)


dao = Dao(host='54.94.237.115', port='5432', user='postgres', password='continente7',
          db='Lindt_BR', schema='info')
queries = []
for root, dirs, files in os.walk(output_dir):
    for forecast_file in files:
        # print(forecast_file)
        query = "COPY info.f00_lindt_forecast FROM '{}' CSV HEADER;".format(os.path.join('/tmp/', forecast_file))
        print(query)
        queries.append(query)
        # print(queries)
        # print(query)
        # dao.run_query(query=query)
        # break
        # df = pd.read_csv(os.path.join(output_dir, forecast_file))
        # break
        # dao.upload_from_dataframe(df, 'aux', if_exists='append')
        # break


