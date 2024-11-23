import datetime


class SmartToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, due_date, importance):
        """
        Add a task to the to-do list.
        :param name: Task description
        :param due_date: Deadline for the task in 'YYYY-MM-DD' format
        :param importance: Importance level from 1 (low) to 5 (high)
        """
        try:
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
            self.tasks.append({
                'name': name,
                'due_date': due_date,
                'importance': importance,
                'priority': None
            })
            self.prioritize_tasks()
            print(f"Task '{name}' added successfully.")
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD'.")

    def prioritize_tasks(self):
        """
        Assigns a priority score to each task based on its due date and importance.
        """
        for task in self.tasks:
            days_left = (task['due_date'] - datetime.datetime.now()).days
            urgency = max(0, 5 - days_left)  # Urgency is higher as due date approaches
            task['priority'] = urgency + task['importance']

        self.tasks.sort(key=lambda t: t['priority'], reverse=True)

    def show_tasks(self):
        """
        Display all tasks in order of priority.
        """
        if not self.tasks:
            print("Your to-do list is empty.")
            return

        print("\nYour Smart To-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            days_left = (task['due_date'] - datetime.datetime.now()).days
            print(f"{idx}. {task['name']}")
            print(f"   Due: {task['due_date'].strftime('%Y-%m-%d')} ({'Overdue' if days_left < 0 else f'{days_left} days left'})")
            print(f"   Importance: {task['importance']}/5")
            print(f"   Priority: {task['priority']}\n")

    def complete_task(self, task_number):
        """
        Mark a task as completed and remove it from the list.
        :param task_number: Index of the task to mark as complete
        """
        if 1 <= task_number <= len(self.tasks):
            completed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{completed_task['name']}' completed and removed from the list.")
        else:
            print("Invalid task number.")


# Example Usage
if __name__ == "__main__":
    todo_list = SmartToDoList()

    # Adding tasks
    todo_list.add_task("Finish project report", "2024-11-25", 5)
    todo_list.add_task("Buy groceries", "2024-11-23", 3)
    todo_list.add_task("Call mom", "2024-11-24", 4)

    # Display tasks
    todo_list.show_tasks()

    # Complete a task
    todo_list.complete_task(2)

    # Display tasks again
    todo_list.show_tasks()
