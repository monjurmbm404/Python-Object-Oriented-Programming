"""
========================================
05_attributes_basics.py
========================================
Attributes:

✔ Variables inside class/object
✔ Store data

Two types:
✔ Class attribute
✔ Instance attribute
"""

class Car:
    # Class attribute
    wheels = 4

# Create object
c1 = Car()
c2 = Car()

# Instance attributes
c1.brand = "Toyota"
c2.brand = "BMW"

print("Car1:", c1.brand, c1.wheels)
print("Car2:", c2.brand, c2.wheels)