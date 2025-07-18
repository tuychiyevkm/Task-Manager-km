from hashlib import sha256


def print_main() -> None:
    print('1. Sign In')
    print('2. Sign Up')
    print('3. Quit')

def is_valid_password(password):
    return len(password) >= 8

def is_valid_name(name):
    return name.replace("'", "").replace(" ", '').isalpha()

def make_password(password):
    return sha256(password.encode()).hexdigest()
