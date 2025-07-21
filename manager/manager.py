import json
from datetime import datetime
from getpass import getpass
from utils import is_valid_password, is_valid_name, make_password, print_satatus
from models import User, Task


class Manager:
    def __init__(self):
        self.user = None
        self.users = self.load_users()

    def register(self):
        name = input("name: ").strip()
        username = input("username: ")
        password = getpass("password: ")
        confirm_password = getpass("confirm password: ")
        if  not is_valid_name(name):
            print('ism xato\n')
        elif self.check_username(username):
            print(f"{username} tanlangan.\n")
        elif password != confirm_password:
            print("password bilan confirm password bir xil emas.\n")
        elif not is_valid_password(password):
            print("xato password.")
        else:
            self.users.append(User(name, username, make_password(password)))
            self.save_users()
            print("muvaffaqiyatli royxatdan otdingiz.")

    def login(self):
        username = input("username: ")
        password = getpass("password: ")

        hashed_password = make_password(password)

        for user in self.users:
            if user.username == username and user.password == hashed_password:
                print_satatus("muvaffaqiyatli kirdingiz.")
                self.user = user
                return True
        print_satatus("user topilmadi.", "error")
        return False

    @staticmethod
    def load_users():
        with open('data/users.json') as jsonfile:
            try:
                data = json.load(jsonfile)
                users = []
                for item in data:
                    user = User.from_dict(item)
                    users.append(user)
                return users
            except:
                return []

    def save_users(self):
        with open('data/users.json', 'w') as jsonfile:
            data = [user.to_dict() for user in self.users]
            json.dump(data, jsonfile, indent=4)

    def check_username(self, username):
        for user in self.users:
            if user.username == username:
                return True
        return False

    def add_task(self):
        title = input('title: ')
        description = input('description: ')
        created_at = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        deatline = input('deatline: ')

        with open('data/tasks.json') as jsonfile:
            try:
                tasks = json.load(jsonfile)
            except:
                tasks = []

        if tasks:
            last_id = tasks[-1]['task_id']
        else:
            last_id = 0

        task = {
            'task_id': last_id + 1,
            'user_id': self.user.user_id,
            'title': title,
            'description': description,
            'created_at': created_at,
            'deatline': deatline,
            'completed': False
        }

        with open('data/tasks.json') as jsonfile:
            try:
                tasks = json.load(jsonfile)
            except:
                tasks = []

        with open('data/tasks.json', 'w') as jsonfile:
            tasks.append(task)
            json.dump(tasks, jsonfile, indent=4)

    def show_tasks(self):

        with open('data/tasks.json') as jsonfile:
            try:
                tasks = json.load(jsonfile)
                tasks = list(filter(
                    lambda task: task['user_id'] == self.user.user_id,
                    tasks
                ))
            except:
                tasks = []

        print("Hamma Tasklar")
        if tasks:
            for counter, task in enumerate(tasks, start=1):
                print(f"{counter}. {task['title']}, {task['completed']}, {task['deatline']}")
        else:
            print("task mavjud emas.")

    def masrk_as_completed(self):

        with open('data/tasks.json') as jsonfile:
            try:
                all_tasks = json.load(jsonfile)
                tasks = list(filter(
                    lambda task: task['user_id'] == self.user.user_id and task['completed'] == False,
                    all_tasks
                ))
            except:
                tasks = []
        
        print("Bajarilmagan Tasklar")
        if tasks:
            for counter, task in enumerate(tasks, start=1):
                print(f"{counter}. {task['title']}, {task['completed']}, {task['deatline']}")
            index = int(input("qaysi taskni bajarildi qilmoqchisiz: "))

            task_id = tasks[index - 1]['task_id']

            with open('data/tasks.json', 'w') as jsonfile:
                for i, task in enumerate(all_tasks):
                    if task['task_id'] == task_id:
                        all_tasks[i]['completed'] = True

                json.dump(all_tasks, jsonfile, indent=4)

            print('bajarildi qilindi.')
        else:
            print("task mavjud emas.")

    def show_incompleted_tasks(self):
        with open('data/tasks.json') as jsonfile:
            try:
                all_tasks = json.load(jsonfile)
                tasks = list(filter(
                    lambda task: task['user_id'] == self.user.user_id and task['completed'] == False,
                    all_tasks
                ))
            except:
                tasks = []
        
        print("Bajarilmagan Tasklar")
        if tasks:
            for counter, task in enumerate(tasks, start=1):
                print(f"{counter}. {task['title']}, {task['completed']}, {task['deatline']}")
