from utils.database_con import *


def task1_run():
    # Get results with sql.
    DatabaseAdmin = DatabaseSQLLite3("input/transactions.db")
    task_result_sql = DatabaseAdmin.ex_simple_command_sql("""select visitor_id, SUM(revenue) from Transactions
                GROUP BY visitor_id
                ORDER BY SUM(revenue) DESC
                LIMIT 1;
                """)
    print("Result From SQL: visitor with ID %s  created %s USD revenue. It is the highest among others. " % task_result_sql[0] )

    # Check it with pandas
    tables_all, tables_names = DatabaseAdmin.get_data_pandas()
    task_result_pandas = tables_all[1][['visitor_id', 'revenue']]
    task_result_pandas = task_result_pandas.groupby(by=["visitor_id"]).sum()
    task_result_pandas = task_result_pandas.sort_values(by=['revenue'], ascending=False )
    print("Result From Pandas: visitor with ID %s  created %s USD revenue. It is the highest among others. " % (task_result_pandas.index[0], task_result_pandas.iloc[0,0]) )

# task1_run()




