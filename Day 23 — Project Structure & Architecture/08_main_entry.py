"""
========================================
main.py
========================================
Main Entry Point:

✔ Connects everything
"""

from models.user import User
from services.payment_service import PaymentService

user = User("Monjur", "monjur@email.com")

payment = PaymentService()
payment.process_payment(user, 1000)