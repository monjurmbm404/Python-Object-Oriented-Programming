"""
========================================
02_type_function_basics.py
========================================
type() function:

✔ Used to check type
✔ Also used to CREATE classes dynamically
"""

# Creating class dynamically using type()
# format:
# type(name, bases, dict)

DynamicClass = type(
    "DynamicClass",
    (),
    {
        "greet": lambda self: "Hello from dynamic class"
    }
)

obj = DynamicClass()

print(obj.greet())
print(type(obj))