"""
========================================
04_factory_improved.py
========================================
Improved Factory:

✔ Easily extendable (OCP)
"""

class Bird:
    def speak(self):
        return "Chirp"

class AnimalFactory:
    _creators = {
        "dog": lambda: Dog(),
        "cat": lambda: Cat(),
        "bird": lambda: Bird()
    }

    @classmethod
    def get_animal(cls, animal_type):
        creator = cls._creators.get(animal_type)
        if creator:
            return creator()
        raise ValueError("Unknown animal")

# reuse Dog, Cat from previous file idea
class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

a = AnimalFactory.get_animal("bird")
print(a.speak())