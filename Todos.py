# src/PAIEA/Todos.py

class Todos:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return f"Task '{task}' has been added."

    def update_task(self, task_index, new_task):
        try:
            self.tasks[task_index] = new_task
            return f"Task at index {task_index} has been updated to '{new_task}'."
        except IndexError:
            return "Invalid task index."

    def retrieve_tasks(self):
        return self.tasks
