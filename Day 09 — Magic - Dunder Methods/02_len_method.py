"""
========================================
02_len_method.py
========================================
__len__:

✔ Defines behavior of len() function
"""

class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

t = Team(["A", "B", "C", "D"])

print("Team size:", len(t))