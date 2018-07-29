import datatime
from api.database import DatabaseConnection


class Entry:

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
