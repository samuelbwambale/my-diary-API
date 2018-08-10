import datetime
import psycopg2
from ..database import DatabaseConnection

now = datetime.datetime.now()

class Entry(DatabaseConnection):

    def __init__(self, title, description, owner_id):
        DatabaseConnection.__init__(self)
        self.title = title
        self.description = description
        self.owner_id = owner_id

    def add_an_entry(self):
        query = "INSERT INTO entries (title, description, owner_id, create_date) VALUES (%s, %s, %s, %s)"
        try:
            self.cursor.execute(query,(
                self.title,
                self.description,
                self.owner_id,
                now.strftime("%Y-%m-%d %H:%M")
                ))
        except psycopg2.Error as e:
            print(e.pgerror)


    def update_an_entry(self, entry_id, description, owner_id):
        query = "UPDATE entries SET description = %s WHERE entry_id = %s AND owner_id = %s"
        self.cursor.execute(query,(description, entry_id, owner_id))
        

    def delete_an_entry(self, entry_id, owner_id):
        query = "DELETE FROM entries WHERE entry_id = %s AND owner_id = %s"
        self.cursor.execute(query, (entry_id, owner_id))
                    
            
    def get_all_entries(self, owner_id):
        query = "SELECT * FROM entries WHERE owner_id = %s"
        self.cursor.execute(query, (owner_id,))
        result = self.cursor.fetchall()
        return result
        

    def get_single_entry_for_user(self, entry_id, owner_id):
        query = "SELECT * FROM entries WHERE entry_id =%s AND owner_id = %s"
        self.cursor.execute(query, (entry_id, owner_id))
        result = self.cursor.fetchone()
        return result


    def get_entry_by_id(self, entry_id):
        query = "SELECT * FROM entries WHERE entry_id = %s"
        self.cursor.execute(query, [entry_id])
        result = self.cursor.fetchone()
        return result

            
    def check_entry_with_title_exists(self, title):
        query = "SELECT * FROM entries WHERE title = %s"
        self.cursor.execute(query, [title])
        result = self.cursor.rowcount
        return result


    def check_entry_with_id_exists( self, entry_id):
        query = "SELECT * FROM entries WHERE entry_id = %s"
        self.cursor.execute(query, [entry_id])
        result = self.cursor.rowcount
        return result
