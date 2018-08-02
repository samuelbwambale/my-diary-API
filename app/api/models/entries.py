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
                now.strftime("%Y-%m-%d")
                ))
        except psycopg2.Error as e:
            print(e.pgerror)


    def update_an_entry(self, entry_id, description, owner_id):
        query = "UPDATE entries SET description = %s WHERE entry_id = %s AND owner_id = %s"
        try:
            self.cursor.execute(query,(description, entry_id, owner_id))
        except psycopg2.Error as e:
            print(e.pgerror)


    def delete_an_entry(self, entry_id, owner_id):
        query = "DELETE FROM entries WHERE entry_id = %s AND owner_id = %s"
        try:
            self.cursor.execute(query, (entry_id, owner_id))
        except psycopg2.Error as e:
            print(e.pgerror)
            
            
    def get_all_entries(self, owner_id):
        query = "SELECT * FROM entries WHERE owner_id = %s"
        try:
            self.cursor.execute(query, (owner_id,))
            result = self.cursor.fetchall()
            return result
        except psycopg.Error as er:
            print(er.pgerror)

    def get_single_entry_for_user(self, entry_id, owner_id)
        query = "SELECT * FROM entries WHERE entry_id AND owner_id = %s"
        try:
            self.cursor.execute(query, (entry_id, owner_id))
            result = self.cursor.fetchall()
            return result
        except psycopg.Error as er:
            print(er.pgerror)


    def get_entry_by_id(self, entry_id):
        query = "SELECT * FROM entries WHERE entry_id = %s"
        try:
            self.cursor.execute(query, [entry_id])
            result = self.cursor.fetchone()
            return result
        except psycopg2.Error as e:
            print(e.pgerror)

            
    def check_entry_with_title_exists(self, title):
        query = "SELECT * FROM entries WHERE title = %s"
        try:
            self.cursor.execute(query, [title])
            result = self.cursor.rowcount
            return result
        except psycopg2.Error as e:
            print(e.pgerror)


    def check_entry_with_id_exists( self, entry_id):
        query = "SELECT * FROM entries WHERE entry_id = %s"
        try:
            self.cursor.execute(query, [entry_id])
            result = self.cursor.rowcount
            return result
        except psycopg2.Error as e:
            print(e.pgerror)
