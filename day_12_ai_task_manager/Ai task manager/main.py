from models.user import User
from services.task_service import TaskService

def main():
    user = User("Sudip")
    service = TaskService(user)

    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Get Recommendation\n4. Exit")
        choice = input("Choice: ")

        if choice == "1":
            title = input("Task title: ")
            priority = int(input("Priority (1-5): "))
            service.add_task(title, priority)

        elif choice == "2":
            service.show_tasks()

        elif choice == "3":
            service.recommend_task()

        elif choice == "4":
            break

if __name__ == "__main__":
    main()