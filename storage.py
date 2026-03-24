import json
import os


class Storage:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)