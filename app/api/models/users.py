from werkzeug.security import generate_password_hash
import uuid


class User:
    def __init__(self, first_name, last_name, email, password):
        self.id = uuid.uuid4().hex
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


def get_user_by_id(user_id):
    for user in USERS:
        if user['user_id'] == user_id: 
            return user


def get_user_by_email(email):
    for user in USERS:
        if user['email'] == email: 
            return user

    
def get_all_users():
    return [user.json() for user in USERS]


def check_if_email_exists(email):
    for user in USERS:
        if user.email == email:
            return user.email
            
    