from flask_login import UserMixin
from sqlite_connector import search_user, search_user_by_id


class User(UserMixin):
    def __init__(self,id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def get(username):
        data = search_user(username)
        return User(data[0], data[1], data[2])

    def get_id(id):
        data = search_user_by_id(id)
        return User(data[0], data[1], data[2])