ENTRIES = []

class Entry:
    def __init__(self, title, description):
        self.entry_id = len(ENTRIES)+1
        self.title = title
        self.description = description


    def add_entry(self):
        ENTRIES.append(self)


    def update_entry(self, title, description):
        self.title = title
        self.description = description


    def delete_entry(self):
        ENTRIES.remove(self)


    def json(self):
        return {
            'entry_id': self.entry_id,
            'title': self.title,
            'description': self.description
       }

            