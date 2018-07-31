import datatime
from api.database import DatabaseConnection

ENTRIES = []
connection = DatabaseConnection()

class Entry:

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.create_date = datetime.datetime.utcnow()
        self.user_id = user_id


    def add_entry(self):
        try:
            query = "INSERT INTO entries (title, description, create_date, owner_id) VALUES (%s, %s, %s,%s)"
            connection.cursor.execute(query,(
                self.title, 
                self.description, 
                self.create_date, 
                self.owner_id))
        except psycopg2.Error as e:
			print(e.pgerror)


    def get_all_entries(self):
		try:
			cur = connection.cursor(cursor_factory=ex.DictCursor)
			query = "SELECT * FROM entries "
            cur.execute(query)
			result = cur.fetchall()
			if  result != [] :				
				return result
			else:
			 	return False
		except psycopg2.Error as e:
			print(e.pgerror)
