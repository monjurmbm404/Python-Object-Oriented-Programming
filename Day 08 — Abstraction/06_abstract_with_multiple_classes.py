"""
========================================
06_abstract_with_multiple_classes.py
========================================
Multiple Implementations:

✔ Same abstract class
✔ Different implementations
"""

from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass

class Email(Notification):
    def send(self, message):
        print("Email sent:", message)

class SMS(Notification):
    def send(self, message):
        print("SMS sent:", message)

class Push(Notification):
    def send(self, message):
        print("Push notification:", message)

channels = [Email(), SMS(), Push()]

for c in channels:
    c.send("Hello User!")