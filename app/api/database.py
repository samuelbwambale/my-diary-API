import psycopg2
from app import app
from config import config
import os



class DatabaseConnection:
    def __init__(self):
        if app.config['TESTING']:
            self.connection = psycopg2.connect("dbname='testdb' user='postgres' password='postgres' host='localhost'")
        # elif app.config['production']:
        #     self.connection = psycopg2.connect(DATABASE_URL)
        # else:
        #     self.connection = psycopg2.connect("dbname='mydiarydb' user='postgres' password='postgres' host='localhost'")
        else:
            DATABASE_URL = 'postgres://hzcloqzitcowiq:f488646797582183b4fae69ae0a96123dabb2e2f221641f16d250e8d7b6f371e@ec2-50-16-196-138.compute-1.amazonaws.com:5432/d53gi9349a1dt1'
            self.connection = psycopg2.connect(DATABASE_URL)

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


if __name__ == "__main__":
    conn = DatabaseConnection()
    conn.create_table_users()
    conn.create_table_entries()
    conn.stop_connection()
