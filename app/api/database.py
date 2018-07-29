from werkzeug.security import check_password_hash
import psycopg2
import psycopg2.extras as ex


class DatabaseConnection(object):

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
        create_table_users_query = ("CREATE TABLE IF NOT EXISTS users \
        (user_id SERIAL PRIMARY KEY, first_name VARCHAR(25) NOT NULL, \
        last_name VARCHAR(25) NOT NULL, email VARCHAR(28) NOT NULL, \
        password VARCHAR(12) NOT NULL)")
        self.cursor.execute(create_table_users_query)
    
    def create_table_entries(self):
        create_table_entries_query = ("CREATE TABLE IF NOT EXISTS entries (entry_id SERIAL PRIMARY KEY, \
        owner_id INTEGER NOT NULL, \
        title VARCHAR(125) NOT NULL,\
        description VARCHAR(255) NOT NULL,\
        create_date timestamp, \
        FOREIGN KEY (owner_id) REFERENCES users (user_id)\
        ON UPDATE CASCADE ON DELETE CASCADE)")
        self.cursor.execute(create_table_entries_query)


    def add_user(self, first_name, last_name, email, password):
        try:
            query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s)"
            self.cursor.execute(query,(first_name, last_name, email, password))
            self.connection.commit()
            self.cursor.close()
        except psycopg2.Error as e:
            print(e.pgerror)

        
    def login_user(self, email, password):
        try:
            self.cursor = self.connection.cursor(cursor_factory=ex.DictCursor)
            query = "SELECT * FROM users WHERE email='"+email+"' "
            result = self.cursor.fetchone()
            if check_password_hash(result['password'], password)
                return result
            else:
                return False
        except psycopg2.Error as e:
            print(e.pgerror)


    def get_all_users(self):
		try:
			self.cursor=self.connection.cursor(cursor_factory=ex.DictCursor)
			query = "SELECT * FROM users "
            self.cursor.execute(query)
			result = self.cursor.fetchall()
			if  result != [] :				
				return result
			else:
			 	return False
		except psycopg2.Error as e:
			print(e.pgerror)


    def add_entry(self, title, description, create_date, user_id):
        try:
            query = "INSERT INTO entries (title, description, create_date, user_id) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(query,(title, description, create_date, user_id))
            self.connection.commit()
            self.cursor.close()
        except psycopg2.Error as e:
            print(e.pgerror)

    
    def get_all_entries(self):
		try:
			self.cursor=self.connection.cursor(cursor_factory=ex.DictCursor)
			query = "SELECT * FROM entries "
            self.cursor.execute(query)
			result = self.cursor.fetchall()
			if  result != [] :				
				return result
			else:
			 	return False
		except psycopg2.Error as e:
			print(e.pgerror)
    
