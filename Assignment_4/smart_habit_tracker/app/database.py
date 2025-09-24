import json
from pathlib import Path

class Database:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            self.write_data([])

    def read_data(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def write_data(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
