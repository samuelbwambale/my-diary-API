from werkzeug.security import generate_password_hash
from api.database import DatabaseConnection
import psycopg2
import psycopg2.extras as ex 

USERS = []
connection = DatabaseConnection()
dict_cur = connection.cursor(cursor_factory=ex.DictCursor)

class User:

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def add_user(self):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s)"
        try:
            connection.cursor.execute(query,(
                self.first_name, 
                self.last_name, 
                self.email, 
                self.password))            
        except psycopg2.Error as e:
            print(e.pgerror)

    def login_user(self, email, password):
        query = "SELECT * FROM users WHERE email = 'email' AND password = 'password'"
        try:
            dict_cur.execute(query,(email, password))
            result = dict_cur.fetchall()
            return result
        except psycopg2.Error as e:
            print(e.pgerror)


    def get_all_users(self):
        query = "SELECT * FROM users"
		try:
            dict_cur.execute(query)
			result = dict_cur.fetchall()
			return result
		except psycopg2.Error as e:
			print(e.pgerror)
