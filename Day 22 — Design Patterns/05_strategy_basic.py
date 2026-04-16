"""
========================================
05_strategy_basic.py
========================================
Strategy Pattern:

✔ Change behavior at runtime
✔ Different algorithms, same interface
"""

class PaymentStrategy:
    def pay(self, amount):
        pass

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} via Card")

class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid {amount} via Cash")

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, amount):
        self.strategy.pay(amount)

# Change behavior dynamically
processor = PaymentProcessor(CardPayment())
processor.process(1000)

processor.strategy = CashPayment()
processor.process(500)