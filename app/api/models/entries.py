import datatime
from api.database import DatabaseConnection
import psycopg2
import psycopg2.extras as ex

ENTRIES = []
connection = DatabaseConnection()
dict_cur = connection.cursor(cursor_factory=ex.DictCursor)

class Entry:

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.create_date = datetime.datetime.utcnow()
        self.user_id = user_id


    def add_an_entry(self):
        query = "INSERT INTO entries (title, description, create_date, owner_id) VALUES (%s, %s, %s,%s)"
        try:
            connection.cursor.execute(query,(
                self.title, 
                self.description, 
                self.create_date, 
                self.owner_id))
        except psycopg2.Error as e:
			print(e.pgerror)


    def update_an_entry(self,description,entry_id):
        query = "UPDATE entries SET description = %s WHERE entry_id = %s"
        try:
            dict_cur.execute(query, (description, entry_id))
        except psycopg2.Error as e:
			print(e.pgerror)


    def delete_an_entry(self, entry_id):
        query = "DELETE FROM entries WHERE entry_id = %s"
        try:
            dict_cur.execute(query, (description, entry_id))
        except psycopg2.Error as e:
			print(e.pgerror)


    def get_all_entries(self):
        query = "SELECT * FROM entries "
		try:
            dict_cur.execute(query)
			result = dict_cur.fetchall()	
			return result
		except psycopg2.Error as e:
			print(e.pgerror)


    def get_entry_by_title(self, title):
        query = "SELECT * FROM entries WHERE title = %s "
        dict_cur.execute(query, title)
        result = dict_cur.fetchone()
        return result

    
