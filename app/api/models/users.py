from werkzeug.security import generate_password_hash

USERS = []

class User:
    def __init__(self, first_name, last_name, email, password):
        self.user_id = len(USERS)+1
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password, method='sha256')


    def add_user(self):
        USERS.append(self)


    def update_user(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


    def delete_user(self):
        USERS.remove(self)


    def json(self):
        return {
            'user_id': self.user_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password
       }
