from flask_login import UserMixin
from sqlite_connector import search_user, search_user_by_id


class User(UserMixin):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def get_id(self):
        data = search_user_by_id(self.id)
        if data is not None:
            return data[0]

    def get(username):
        data = search_user(username)
        if data is not None:
            return User(data[0], data[1], data[2])

    def get_object(id):
        data = search_user_by_id(id)
        if data is not None:
            return User(data[0], data[1], data[2])