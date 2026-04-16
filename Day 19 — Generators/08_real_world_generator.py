"""
========================================
08_real_world_generator.py
========================================
Real-world Example:

✔ Streaming large data files
"""

def read_lines(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

# Example usage (file assumed)
# for line in read_lines("data.txt"):
#     print(line)