from utils.database_con import *


def task2_run():
    # Get results with sql.
    DatabaseAdmin = DatabaseSQLLite3("input/transactions.db")
    get_devices = DatabaseAdmin.ex_simple_command_sql("""select id from Devices
                Where device_name = 'Mobile Phone';
                """)
    get_device_mobile = get_devices[0][0]


    task_result_sql = DatabaseAdmin.ex_simple_command_sql("""select datetime , SUM(revenue) from Transactions
                Where device_type = """+  str(get_device_mobile)+"""
                GROUP BY datetime
                ORDER BY SUM(revenue) DESC
                LIMIT 1;
                """)
    print("Result From SQL: %s day was the most profitable (about  %s USD revenue) for mobile devices." % task_result_sql[0] )

    # # Check it with pandas
    tables_all, tables_names = DatabaseAdmin.get_data_pandas()
    task_result_pandas = tables_all[1]
    task_result_pandas = task_result_pandas.loc[task_result_pandas['device_type']==3].reset_index(drop=True)
    task_result_pandas['datetime'] = pd.to_datetime(task_result_pandas['datetime'], format='%Y-%m-%d')
    task_result_pandas = task_result_pandas[['datetime', 'revenue']]
    task_result_pandas = task_result_pandas.groupby(by=["datetime"]).sum()
    task_result_pandas = task_result_pandas.sort_values(by=['revenue'], ascending=False )
    print("Result From Pandas: %s day was the most profitable (about  %s USD revenue) for mobile devices." % (task_result_pandas.index[0], task_result_pandas.iloc[0,0]) )

# task2_run()