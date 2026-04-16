"""
========================================
09_practice_dynamic_class.py
========================================
Practice: Dynamic Class Creation
"""

def say_hi(self):
    return "Hi from dynamic class"

Dynamic = type(
    "Dynamic",
    (),
    {"say_hi": say_hi}
)

obj = Dynamic()

print(obj.say_hi())