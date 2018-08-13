import psycopg2

class DatabaseConnection:
    def __init__(self):
        self.connection = psycopg2.connect("dbname='mydiarydb' user='postgres' password='postgres' host='localhost'")
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()        


    def create_table_users(self):
        try:
            query = "CREATE TABLE IF NOT EXISTS users (user_id SERIAL PRIMARY KEY, first_name VARCHAR(25) NOT NULL, last_name VARCHAR(25) NOT NULL, email VARCHAR(25) NOT NULL, password VARCHAR(15) NOT NULL)"
            self.cursor.execute(query)
            print("Users table created")
        except psycopg2.Error as e:
            print(e.pgerror)
            

    def create_table_entries(self):
        try:
            query = "CREATE TABLE IF NOT EXISTS entries (entry_id SERIAL PRIMARY KEY, owner_id INTEGER NOT NULL, title VARCHAR(255) NOT NULL, description VARCHAR(255) NOT NULL, create_date timestamp, FOREIGN KEY (owner_id) REFERENCES users (user_id) ON UPDATE CASCADE ON DELETE CASCADE)"
            self.cursor.execute(query)
            print("Entries table created")
        except psycopg2.Error as e:
            print(e.pgerror)


    def drop_table_users(self):
        query = "DROP TABLE IF EXISTS users CASCADE"
        self.cursor.execute(query)


    def drop_table_entries(self):
        query = "DROP TABLE IF EXISTS entries CASCADE"
        self.cursor.execute(query)
        

    def stop_connection(self):
        self.cursor.close()
        self.connection.close()
