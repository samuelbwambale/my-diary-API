from werkzeug.security import generate_password_hash
from api.database import DatabaseConnection

USERS = []
connection = DatabaseConnection()

class User:

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def add_user(self):
        try:
            query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s)"
            connection.cursor.execute(query,(
                self.first_name, 
                self.last_name, 
                self.email, 
                self.password))
            
        except psycopg2.Error as e:
            print(e.pgerror)

    def login_user(self, email, password):
        try:
            cur = connection.cursor(cursor_factory=ex.DictCursor)
            query = "SELECT * FROM users WHERE email = 'email' AND password = 'password'"
            cur.execute(query,(email, password))
            result = cur.fetchall()
            if  result != []:
                return result
            else:
                return False
        except psycopg2.Error as e:
            print(e.pgerror)


    def get_all_users(self):
		try:
			self.cursor=self.connection.cursor(cursor_factory=ex.DictCursor)
			query = "SELECT * FROM users"
            self.cursor.execute(query)
			result = self.cursor.fetchall()
			if  result != []:				
				return result
			else:
			 	return False
		except psycopg2.Error as e:
			print(e.pgerror)
