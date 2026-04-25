class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority
        self.completed = False

    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.title} | Priority: {self.priority} | {status}"