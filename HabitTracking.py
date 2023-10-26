# src/PAIEA/HabitTracking.py

class HabitTracking:
    def __init__(self):
        self.habits = {}

    def add_habit(self, habit_name, habit_details):
        if habit_name not in self.habits:
            self.habits[habit_name] = habit_details
            return f"Habit '{habit_name}' added successfully."
        else:
            return f"Habit '{habit_name}' already exists."

    def update_habit(self, habit_name, habit_details):
        if habit_name in self.habits:
            self.habits[habit_name] = habit_details
            return f"Habit '{habit_name}' updated successfully."
        else:
            return f"Habit '{habit_name}' does not exist."

    def retrieve_habit(self, habit_name):
        if habit_name in self.habits:
            return self.habits[habit_name]
        else:
            return f"Habit '{habit_name}' does not exist."
