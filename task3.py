from utils.database_con import *


def task3_run():
    url_save_pandas = 'output/pd_combined.csv'
    url_save_sql = 'output/sql_combined.csv'

    # Get results with sql.
    DatabaseAdmin = DatabaseSQLLite3("input/transactions.db")

    task_result_sql = DatabaseAdmin.ex_dataframe_from_sql("""
    select Transactions.id, Transactions.datetime, Transactions.visitor_id, Transactions.device_type, Transactions.revenue, Transactions.tax, Devices.device_name 
    from Transactions
    INNER JOIN Devices
    ON Transactions.device_type=Devices.id;
    """)
    task_result_sql.to_csv(url_save_sql, index = False)
    print("Result From SQL: Combined File saved to path: %s " % url_save_sql )

 
    # # Check it with pandas
    tables_all, tables_names = DatabaseAdmin.get_data_pandas()
    device_table = tables_all[0]
    transaction_table = tables_all[1]
    device_table.rename(columns = {'id':'fk'}, inplace = True)
    task_result_pandas = pd.merge(transaction_table, device_table, left_on = 'device_type', right_on = 'fk').drop(['fk'], axis=1)
    task_result_pandas = task_result_pandas.sort_values(by=['id'] ).reset_index(drop=True)
    task_result_pandas.to_csv(url_save_pandas, index = False)
    print("Result From Pandas: Combined File saved to path: %s " % url_save_pandas )
    # print(task_result_pandas.drop(['device_name'], axis=1).equals(transaction_table))
    

# task3_run()