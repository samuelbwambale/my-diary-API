from werkzeug.security import generate_password_hash
from api.database import Database

class User:
    connection = Database()
    cursor = connection.cursor
    dict_cursor = connection.dict_cursor

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password, method='sha256')


    
    

    def get_user_by_email(self):
        try:
            query = "SELECT * FROM users WHERE email = %s "
            User.dict_cursor.execute(query, [self.email])
            usr = User.dict_cursor.fetchone()
            return usr
        except psycopg2.Error as e:
            print(e.pgerror)
