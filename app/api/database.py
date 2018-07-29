import psycopg2

class Database:

    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                dbname = 'mydiarydb'
                user = 'postgres'
                password = 'postgres'
                host =  '127.0.0.1'
                port = '5432')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("Connection successfull")
        except:
            print("Connection failed.")


    def create_table_users(self):
        create_table_users_query = ("CREATE TABLE IF NOT EXISTS users (user_id SERIAL PRIMARY KEY, name VARCHAR(20) NOT NULL, email VARCHAR(28) NOT NULL, password VARCHAR(12) NOT NULL)")
        self.cursor.execute(create_table_users_query)
    
    def create_table_entries(self):
        create_table_entries_query = ("CREATE TABLE IF NOT EXISTS entries (entry_id SERIAL PRIMARY KEY,user_id INTEGER NOT NULL,title VARCHAR(255) NOT NULL,description VARCHAR(255) NOT NULL,creation_time timestamp,FOREIGN KEY (user_id)REFERENCES users (user_id)ON UPDATE CASCADE ON DELETE CASCADE)")
        self.cursor.execute(create_table_entries_query)