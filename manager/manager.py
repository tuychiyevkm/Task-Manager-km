
from getpass import getpass
from models import User
from utils import is_valid_password


class Manager:
    def __init__(self):
        self.user = None

    def register(self):
        name = input("name: ").strip()
        if not name.replace("'", "").replace(" ", '').isalpha():
            print('Ism xato\n')
            return

        username = input("username: ")
        if User.check_username(username):
            print(f"{username} band.\n")
            return

        password = getpass("password: ")
        confirm_password = getpass("confirm password: ")
        if password != confirm_password or not is_valid_password(password):
            print("Parol xato yoki kuchsiz.\n")
            return

        self.user = User(name, username, password)
        print("Ro'yxatdan o'tish muvaffaqiyatli.\n")

    def login(self):
        username = input("username: ")
        password = getpass("password: ")
        user = User.authenticate(username, password)
        if user:
            self.user = user
            print(f"Xush kelibsiz, {self.user.name}!\n")
        else:
            print("Login yoki parol noto‘g‘ri.\n")

