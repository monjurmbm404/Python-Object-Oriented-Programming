"""
========================================
07_real_world_iterator.py
========================================
Real-world Iterator:

✔ Pagination / streaming data idea
"""

class DataStream:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        raise StopIteration

stream = DataStream(["User1", "User2", "User3"])

for user in stream:
    print("Processing:", user)