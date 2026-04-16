"""
========================================
07_practice_car.py
========================================
Practice: Car Class
"""

class Car:
    brand = ""
    speed = 0

# Create objects
c1 = Car()
c2 = Car()

# Assign values
c1.brand = "Tesla"
c1.speed = 200

c2.brand = "BMW"
c2.speed = 180

print("Car 1:", c1.brand, c1.speed)
print("Car 2:", c2.brand, c2.speed)