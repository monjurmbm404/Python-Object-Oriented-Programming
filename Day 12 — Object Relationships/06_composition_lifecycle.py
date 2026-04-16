"""
========================================
06_composition_lifecycle.py
========================================
Composition Lifecycle:

✔ If parent is destroyed → child also destroyed
"""

class Heart:
    def beat(self):
        print("Heart beating")

class Human:
    def __init__(self):
        self.heart = Heart()  # strong dependency

    def live(self):
        self.heart.beat()
        print("Human alive")

h = Human()
h.live()

# If 'h' is deleted → heart also gone