import datatime
from api.database import DatabaseConnection


class Entry:

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.create_date = datetime.datetime.utcnow()
        self.user_id = user_id
