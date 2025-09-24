from typing import List
from app.database import Database

class Habit:
    def __init__(self, id: int, name: str, goal: int, progress: int = 0):
        self.id = id
        self.name = name
        self.goal = goal
        self.progress = progress

    def mark_done(self):
        if self.progress < self.goal:
            self.progress += 1

class HabitManager:
    def __init__(self, db: Database):
        self.db = db
        self.habits: List[Habit] = self.load_habits()

    def load_habits(self):
        data = self.db.read_data()
        return [Habit(**habit) for habit in data]

    def get_all_habits(self):
        return self.habits

    def add_habit(self, name: str, goal: int):
        habit_id = max([h.id for h in self.habits], default=0) + 1
        habit = Habit(habit_id, name, goal)
        self.habits.append(habit)
        self.save()

    def delete_habit(self, habit_id: int):
        self.habits = [h for h in self.habits if h.id != habit_id]
        self.save()

    def mark_done(self, habit_id: int):
        for h in self.habits:
            if h.id == habit_id:
                h.mark_done()
        self.save()

    def save(self):
        data = [h.__dict__ for h in self.habits]
        self.db.write_data(data)
