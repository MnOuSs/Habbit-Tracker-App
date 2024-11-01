from datetime import datetime

class HabitManager:
    def __init__(self):
        self.habits = []  # List to store all Habit objects

    def add_habit(self, habit):
        self.habits.append(habit)

    def delete_habit(self, habit_name):
        self.habits = [habit for habit in self.habits if habit.name != habit_name]

    def update_habit(self, habit_name, new_attributes):
        for habit in self.habits:
            if habit.name == habit_name:
                habit.__dict__.update(new_attributes)

    def complete_habit(self, habit_name):
        for habit in self.habits:
            if habit.name == habit_name:
                habit.completions.append(datetime.now())
