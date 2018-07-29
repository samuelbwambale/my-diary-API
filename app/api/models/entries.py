import uuid
import datatime

ENTRIES = []

class Entry:
    def __init__(self, title, description):
        self.id = uuid.uuid4().hex
        self.title = title
        self.description = description
        self.created_date = datetime.datetime.utcnow()


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


def get_entry_by_id(entry_id):
    for entry in ENTRIES:
        if entry['entry_id'] == entry_id: 
            return entry



def get_entry_by_title(title):
    for entry in ENTRIES:
        if entry['title'] == title: 
            return entry

def get_all_entries():
    return [entry.json() for entry in ENTRIES]
            