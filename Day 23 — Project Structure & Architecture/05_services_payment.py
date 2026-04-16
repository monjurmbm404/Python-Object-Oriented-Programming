"""
========================================
services/payment_service.py
========================================
Service Layer:

✔ Contains business logic
✔ Works with models
"""

class PaymentService:
    def process_payment(self, user, amount):
        print(f"{user.name} paid {amount}")