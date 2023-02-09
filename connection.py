import psycopg2 as pg2


def connect_with_database( conn, cur, host, db, user, password ):
    #Try to make the connection with the Database (Postgres)
    try:
        conn = pg2.connect(f'host={host} dbname={db} user={user} password={password}')

        #Use the connection to get a cursor that can be used to execute queries
        cur = conn.cursor()

        # Set automatic commit to be true so that each action is commited without 
        # having to call conn.commit() after each command
        conn.set_session(autocommit=True)
    except pg2.Error as e:
        print(f'Error: Could not make connection to the {db} Database')
        print(e)

    return conn, cur

def close_connection( conn ):
    #Close the connection with database
    try:
        conn.close()
    except pg2.Error as e:
        print('Could not close connection')
        print(e)
