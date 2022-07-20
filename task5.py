from utils.database_con import *


def task5_run():
    # Get results with sql.
    DatabaseAdmin = DatabasePostgreSQL()
    try:
        get_devices = DatabaseAdmin.ex_simple_command_sql("""SELECT * FROM information_schema.tables;
                    """)
        print('Successful connection with ElephantSQL (for PostgreSQL).')
        print('Similar approach could be used to add support for other DBMS as well.')
    except:
        print('Error, please check credentials.')

# task5_run()




