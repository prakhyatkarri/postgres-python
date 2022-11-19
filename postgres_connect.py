from psycopg2 import connect
 
HOST = 'localhost'
USERNAME = "postgres"
PASSWORD = "postgres"
CONNECTION_STRING = f"dbname='postgres' host='{HOST}' user='{USERNAME}' password='{PASSWORD}'"
 
def connect_to_db():
    connection = connect(CONNECTION_STRING)

    if connection is not None and connection.status == 1:
        print('Connection Successful !!')
        return connection
    else:
        print("Connection Failed.")
        
# connect_to_db()