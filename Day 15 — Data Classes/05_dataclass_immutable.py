"""
========================================
05_dataclass_immutable.py
========================================
Immutability:

✔ frozen=True makes object immutable
✔ Cannot change values after creation
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    api_key: str
    timeout: int

c = Config("ABC123", 30)

print(c.api_key)

# c.api_key = "NEW" ❌ Error (immutable)