from utils import print_main, save_data, load_data
from manager import Manager
from models.task import Task
from models.user import User

def main():
    load_data()  # <<< eski ma’lumotlarni yuklash

    m = Manager()
    while True:
        print_main()
        choice = input("Tanlang (1-3): ")

        if choice == "1":
            m.login()
        elif choice == "2":
            m.register()
        elif choice == "3":
            save_data(User.users)  # <<< chiqishdan oldin saqlash
            print("Chiqildi.")
            break
        else:
            print("Noto‘g‘ri tanlov.\n")
            continue

        while m.user:
            print("\n1. Vazifa qo‘shish\n2. Vazifalarni ko‘rish\n3. Vazifani bajarilgan deb belgilash\n4. Chiqish")
            sub = input("Tanlang: ")

            if sub == "1":
                title = input("Sarlavha: ")
                desc = input("Tavsif: ")
                deadline = input("Muddat (YYYY-MM-DD): ")
                task = Task(title, desc, deadline)
                m.user.tasks.append(task)
                print("Vazifa qo‘shildi.\n")

            elif sub == "2":
                if not m.user.tasks:
                    print("Sizda hali vazifa yo‘q.")
                else:
                    for i, task in enumerate(m.user.tasks, 1):
                        print(f"{i}. {task}")

            elif sub == "3":
                if not m.user.tasks:
                    print("Sizda hali vazifa yo‘q.")
                else:
                    for i, task in enumerate(m.user.tasks, 1):
                        print(f"{i}. {task}")
                    idx = int(input("Qaysi vazifa bajarildi? (raqam): "))
                    if 0 < idx <= len(m.user.tasks):
                        m.user.tasks[idx - 1].mark_as_completed()
                        print("✅ Belgilandi.")

            elif sub == "4":
                save_data(User.users)  # <<< foydalanuvchi chiqsa, saqlaymiz
                m.user = None
                print("Chiqildi.\n")
            else:
                print("Xato tanlov.")
