import json
from models.user import User
from models.task import Task

def print_main() -> None:
    print('1. Sign In')
    print('2. Sign Up')
    print('3. Quit')

def is_valid_password(password):
    return True

DATA_FILE = 'data/tasks.json'

def save_data(users):
    data = []
    for user in users:
        data.append({
            'user_id': user.user_id,
            'name': user.name,
            'username': user.username,
            'password': user.password,
            'tasks': [
                {
                    'title': task.title,
                    'description': task.description,
                    'created_at': task.created_at,
                    'deadline': task.deadline,
                    'completed': task.completed
                }
                for task in user.tasks
            ]
        })

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)

        for user_data in data:
            user = User(
                user_data['name'],
                user_data['username'],
                user_data['password'],  # BU allaqachon hashed
            )
            user.password = user_data['password']
            user.user_id = user_data['user_id']
            user.tasks = []
            for task_data in user_data['tasks']:
                task = Task(
                    task_data['title'],
                    task_data['description'],
                    task_data['deadline']
                )
                task.created_at = task_data['created_at']
                task.completed = task_data['completed']
                user.tasks.append(task)

    except FileNotFoundError:
        pass  
