from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M')
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __repr__(self):
        status = "✅" if self.completed else "❌"
        return f"{status} {self.title} — muddat: {self.deadline}"