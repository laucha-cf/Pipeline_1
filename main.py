from connection import connect_with_database, close_connection
from database import create_database, create_table

#Data for connection with Postgres
HOST = 'localhost'
DB_DEFAULT = 'postgres'
USER = 'postgres'
PASS = 'postgres'

#Data for the database and table
DB_NEW = 'rentprice'
TABLE_NAME = 'Barcelona'

#Global variables
conn = None
cur = None

if __name__ == '__main__':
    #First, we connect with "postgres" database because is the only that exists
    conn, cur = connect_with_database( conn, cur, HOST, DB_DEFAULT, USER, PASS )

    #Once there, we create our new database
    create_database( cur, DB_NEW )

    #Close that connection
    close_connection( conn )

    #Make a new connection (with our new db)
    new_conn, new_cur = connect_with_database( conn, cur, HOST, DB_NEW, USER, PASS )

    create_table( new_cur, TABLE_NAME )

    close_connection( new_conn )

    