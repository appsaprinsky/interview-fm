import sqlite3
import pandas as pd
import psycopg2

class DatabaseSQLLite3:

    def __init__(self, url_input):   #"input/transactions.db"
        self.url_input = url_input

    def ex_simple_command_sql(self, input_command):
        con = sqlite3.connect(self.url_input)
        cur = con.cursor()
        cur.execute(input_command)
        result = cur.fetchall()
        cur.close()
        con.close()
        return result

    def ex_dataframe_from_sql(self, input_command):
        con = sqlite3.connect(self.url_input)
        cur = con.cursor()
        result = pd.read_sql_query(input_command, con)
        cur.close()
        con.close()
        return result        

    def get_data_pandas(self):
        con = sqlite3.connect(self.url_input)
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        coll_tables = []
        names_tables = []
        for table_name in tables:
            table_name = table_name[0]
            table = pd.read_sql_query("SELECT * from %s" % table_name, con)
            coll_tables.append(table)
            names_tables.append(table_name)
        cursor.close()
        con.close()
        return coll_tables, names_tables




class DatabasePostgreSQL:

    def ex_simple_command_sql(self, input_command):
        con = psycopg2.connect("dbname='oiaionct' user='oiaionct' host='abul.db.elephantsql.com'  password='dnXgpwNkBsxrDZas37SzZkY5jJRfz7Yl' ")
        cur = con.cursor()
        cur.execute(input_command)
        result = cur.fetchall()
        cur.close()
        con.close()
        return result





