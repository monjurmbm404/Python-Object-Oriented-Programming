"""
========================================
08_practice_score_system.py
========================================
Practice: Score System
"""

class Score:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Score(self.value + other.value)

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return f"Score: {self.value}"

s1 = Score(70)
s2 = Score(80)

print(s1 + s2)
print(s1 > s2)
print(s1 == s2)