from postgres_connect import connect_to_db


def get_connection():
    return connect_to_db()

def execute(record, connection, return_result=None):
    try:
        cursor = connection.cursor()
        cursor.execute(record)
        connection.commit()
        
        if return_result:
            return cursor.fetchall()
    except Exception as e:
        print(f"Exception in execute: {e}")

def create_table(connection):
    return execute("CREATE TABLE IF NOT EXISTS product ( \
  id INT NOT NULL, \
  name varchar(30) NOT NULL, \
  PRIMARY KEY (id) \
);  ", connection)


def insert_record(connection):
    return execute("INSERT INTO PRODUCT (ID, NAME) VALUES (1, 'Apple') ;", connection)

def select_record(connection):
    return execute("SELECT * FROM PRODUCT ;", connection, True)
    

connection = get_connection()
print(create_table(connection))
print(insert_record(connection))
print(select_record(connection))