from utils.database_con import *
import pandas as pd
import numpy as np
import sys


def task4_run(input_curr = 'USD'):
    input_data = pd.read_xml('input/eurofxref-hist-90d.xml', xpath=".//doc:Cube",
                            namespaces={"doc":"http://www.ecb.int/vocabulary/2002-08-01/eurofxref"})   
    
    input_data = input_data.drop(['Cube'], axis=1)
    input_data['time'].fillna(method = 'ffill', inplace = True)
    input_data = input_data.dropna()
    input_data = input_data.loc[input_data['currency'] == input_curr].reset_index(drop = True)

    if len(input_data) <= 0:
        print('Cannot find Currency')
        sys.exit()


    DatabaseAdmin = DatabaseSQLLite3("input/transactions.db")
    data_from_original = DatabaseAdmin.ex_dataframe_from_sql("""
    select * from Transactions
    """)

    init_exchange = input_data.iloc[-1,2] # if latest day for exchange rate won't be found, we will use this default value.
    for i in range(len(data_from_original)):
        id_c = data_from_original.iloc[i,0]
        time_c = data_from_original.iloc[i,1]
        time_c = pd.to_datetime(time_c).strftime("%Y-%m-%d")
        revenue_c = data_from_original.iloc[i,4]

        rate_value_c = input_data.loc[input_data['time'] <= time_c]
        if len(rate_value_c) > 0:
            rate_value_c = rate_value_c.reset_index(drop=True)
            data_from_original.iloc[i,4] = revenue_c/rate_value_c.iloc[0,2]
        else:
            data_from_original.iloc[i,4] = revenue_c/init_exchange

    data_from_original.to_csv('output/task4_result.csv')
    conn = sqlite3.connect("input/transactions_4.db")
    data_from_original.to_sql("Transactions",conn,if_exists='replace',index=False, index_label="id")
    conn.close()
    print("Please check file input/transactions_4.db to see changes! You can also see changes in file output/task4_result.csv")



# task4_run()