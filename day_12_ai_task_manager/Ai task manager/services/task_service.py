from models.task import Task
from services.recommendation import RecommendationEngine

class TaskService:
    def __init__(self, user):
        self.user = user
        self.recommender = RecommendationEngine()

    def add_task(self, title, priority):
        task = Task(title, priority)
        self.user.add_task(task)
        print("Task added.")

    def show_tasks(self):
        for t in self.user.tasks:
            print(t)

    def recommend_task(self):
        task = self.recommender.get_best_task(self.user.tasks)
        if task:
            print("Recommended:", task)
        else:
            print("No tasks available.")