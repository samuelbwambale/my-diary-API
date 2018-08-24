import datetime
import psycopg2
from ..database import DatabaseConnection

now = datetime.datetime.now()

class Entry(DatabaseConnection):
    """ Entry class """

    def __init__(self, title, description, owner_id):
        DatabaseConnection.__init__(self)
        self.title = title
        self.description = description
        self.owner_id = owner_id

    def add_an_entry(self):
        """ Add an entry into the entries table """
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
        """ Update an existing entry """
        query = "UPDATE entries SET description = %s WHERE entry_id = %s AND owner_id = %s"
        self.cursor.execute(query,(description, entry_id, owner_id))
        

    def delete_an_entry(self, entry_id, owner_id):
        """ Delete an entry from entries table """
        query = "DELETE FROM entries WHERE entry_id = %s AND owner_id = %s"
        self.cursor.execute(query, (entry_id, owner_id))
                    
            
    def get_all_entries(self, owner_id):
        """ Fetch all entries of a particular user """
        query = "SELECT * FROM entries WHERE owner_id = %s"
        self.cursor.execute(query, (owner_id,))
        result = self.cursor.fetchall()
        return result


    def get_single_entry_for_user(self, entry_id, owner_id):
        """ Fetch a single entry of a user """
        query = "SELECT * FROM entries WHERE entry_id =%s AND owner_id = %s"
        self.cursor.execute(query, (entry_id, owner_id))
        result = self.cursor.fetchone()
        return result

            
    def check_entry_with_title_exists(self, title):
        """ Check if there exists an entry with parsed title """
        query = "SELECT * FROM entries WHERE title = %s"
        self.cursor.execute(query, [title])
        result = self.cursor.rowcount
        return result

