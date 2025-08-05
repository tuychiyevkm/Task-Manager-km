from hashlib import sha256

class User:
    users = []

    def __init__(self, name, username, password, hash_password=True):
        if hash_password:
            self.password = sha256(password.encode()).hexdigest()
        else:
            self.password = password

        self.user_id = len(User.users) + 1
        self.name = name
        self.username = username
        self.tasks = []

        User.users.append(self)

    @classmethod
    def check_username(cls, username):
        return any(user.username == username for user in cls.users)

    @classmethod
    def authenticate(cls, username, password):
        hashed = sha256(password.encode()).hexdigest()
        for user in cls.users:
            if user.username == username and user.password == hashed:
                return user
        return None
