"""
========================================
03_dependency_injection_test.py
========================================
Dependency Injection:

✔ Replace real dependency with fake/mock
"""

class FakeGateway:
    def pay(self):
        return True

class Payment:
    def __init__(self, gateway):
        self.gateway = gateway

    def process(self):
        return self.gateway.pay()

# Testing with fake object
payment = Payment(FakeGateway())

print(payment.process())  # True