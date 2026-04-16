"""
========================================
01_dry_principle.py
========================================
DRY → Don't Repeat Yourself

❌ BAD: Repeating same logic multiple times
✔ GOOD: Reuse code (functions/classes)
"""

# ❌ BAD APPROACH (code duplication)
def area_circle(radius):
    return 3.14 * radius * radius

def area_sphere(radius):
    return 4 * 3.14 * radius * radius  # repeating formula part

# ✔ GOOD APPROACH (DRY)
def circle_area(radius):
    return 3.14 * radius * radius

def sphere_area(radius):
    return 4 * circle_area(radius)  # reuse function

print(circle_area(5))
print(sphere_area(5))