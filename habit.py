from datetime import datetime

class Habit:
    def __init__(self, name: str, description: str, periodicity: str):
        self.name = name                    # Title of the habit (e.g., "Exercise")
        self.description = description      # Brief description of the habit
        self.periodicity = periodicity      # Frequency (e.g., "daily", "weekly")
        self.creation_date = datetime.now() # Date the habit was created
        self.completions = []               # List to store completion timestamps

    def __repr__(self):
        return (f"Habit(name='{self.name}', description='{self.description}', "
                f"periodicity='{self.periodicity}', creation_date='{self.creation_date}', "
                f"completions={self.completions})")
