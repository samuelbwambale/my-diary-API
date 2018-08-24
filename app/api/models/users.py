import psycopg2
from app.api.database import DatabaseConnection


class User(DatabaseConnection):
    """ User class """

    def __init__(self, first_name, last_name, email, password):
        DatabaseConnection.__init__(self)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


    def add_user(self):
        """ Add a new user to the users table """
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
        """ Get a user with this username and password """
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        self.cursor.execute(query,(email, password))
        result = self.cursor.fetchone()
        return result


    def get_all_users(self):
        """ Fetch all existing users """
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result


    def get_user_by_email(self, email):
        """ Get a user by email """
        query = "SELECT * FROM users WHERE email = %s"
        self.cursor.execute(query,[email])
        result = self.cursor.rowcount
        return result

    def get_user_by_id(self, user_id):
        """ Get a user by id """
        query = "SELECT * FROM users WHERE user_id = %s"
        self.cursor.execute(query,[user_id])
        result = self.cursor.fetchone()
        return result
