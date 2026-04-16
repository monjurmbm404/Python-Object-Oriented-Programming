"""
========================================
04_iterator_with_data.py
========================================
Iterator with Data:

✔ Iterate over custom list inside class
"""

class Team:
    def __init__(self, members):
        self.members = members
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.members):
            member = self.members[self.index]
            self.index += 1
            return member
        else:
            raise StopIteration

team = Team(["A", "B", "C"])

for member in team:
    print(member)