from getpass import getpass
from models import User
from utils import is_valid_password


class Manager:
    def __init__(self):
        self.user = None

    def register(self):
        name = input("name: ").strip()
        if  not name.replace("'", "").replace(" ", '').isalpha():
            print('ism xato\n')
        username = input("username: ")
        if User.check_username(username):
            print(f"{username} tanlangan.\n")
        password = getpass("password: ")
        confirm_password = getpass("confirm password: ")
        if password != confirm_password and not is_valid_password(password):
            print("password xato.\n")
        
        self.user = User(name, username, password)
