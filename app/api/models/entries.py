import datatime
from api.database import DatabaseConnection

ENTRIES = []

class Entry:
    connection = Database()
    cursor = connection.cursor
    dict_cursor = connection.dict_cursor


    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.create_date = datetime.datetime.utcnow()
        self.user_id = user_id


    def add_entry(self):
        query = "INSERT INTO entries (title, description, create_date, user_id) VALUES (%s, %s, %s)"
        User.cursor.execute(query,(
            self.title, 
            self.description, 
            self.create_date, 
            self.user_id))

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
