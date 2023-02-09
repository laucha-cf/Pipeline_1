import psycopg2 as pg2

def create_database( cur, dbname ):
    # Create a Database
    try:
        cur.execute(f'CREATE DATABASE IF NOT EXISTS {dbname}')
    except pg2.Error as e:
        print('Could not create the database because of the following error')
        print(e)

def create_table( cur, table_name ):

    try:
        cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (
            year INT,
            trimester INT,
            district VARCHAR,
            neighbourhood VARCHAR,
            average_rent VARCHAR,
            price FLOAT
        );""" )
    except pg2.Error as e:
        print(f'Error: Could not create the table {table_name}')
        print(e)

def insert_data( cur, table, dataframe ):
    #Insert all data in our table
    for row in dataframe:
        try:
            cur.execute(f"""
            INSERT INTO {table} (
                year,
                trimester,
                district,
                neighbourhood,
                average_rent,
                price)
            VALUES (
                
                )
            """)
        except pg2.Error as e:
            print(e)