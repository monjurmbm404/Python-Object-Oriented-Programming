"""
========================================
03_factory_basic.py
========================================
Factory Pattern:

✔ Creates objects without exposing logic
✔ User doesn't know exact class
"""

class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

class AnimalFactory:
    @staticmethod
    def get_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            return None

animal = AnimalFactory.get_animal("dog")
print(animal.speak())