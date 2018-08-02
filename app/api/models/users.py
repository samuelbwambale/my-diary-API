import psycopg2
from app.api.database import DatabaseConnection


class User(DatabaseConnection):

    def __init__(self, first_name, last_name, email, password):
        DatabaseConnection.__init__(self)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


    def add_user(self):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        try:
            self.cursor.execute(query,(
                self.first_name, 
                self.last_name, 
                self.email, 
                self.password))            
        except psycopg2.Error as e:
            print(e.pgerror)

    
    def login_user(self, email, password):
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        try:
            self.cursor.execute(query,(email, password))
            result = self.cursor.fetchone()
            return result
        except psycopg2.Error as e:
            print(e.pgerror)


    def get_all_users(self):
        query = "SELECT * FROM users"
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except psycopg2.Error as e:
            print(e.pgerror)


    def get_a_user(self, email):
        query = "SELECT * FROM users WHERE email = %s"
        try:
            self.cursor.execute(query,[email])
            result = self.cursor.fetchall()
            return result
        except psycopg2.Error as e:
            print(e.pgerror)


    def get_user_by_email(self, email):
        query = "SELECT * FROM users WHERE email = %s"
        try:
            self.cursor.execute(query,[email])
            result = self.cursor.rowcount
            return result
        except psycopg2.Error as e:
            print(e.pgerror)
