from hashlib import sha256

class User:
    users = []

    def __init__(self, name, username, password):
        hashed_password = sha256(password.encode()).hexdigest()

        self.user_id = 1
        self.name = name
        self.username = username
        self.pasword = hashed_password

        User.users.append(self)

    @classmethod
    def check_username(cls, username):
        for user in cls.users:
            if user.username == username:
                return True
        return False
