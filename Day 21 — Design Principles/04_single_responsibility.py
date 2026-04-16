"""
========================================
04_single_responsibility.py
========================================
Single Responsibility Principle (SRP):

✔ One class = One job
"""

# ❌ BAD (multiple responsibilities)
class Report:
    def generate(self):
        print("Generating report")

    def save(self):
        print("Saving report")

# ✔ GOOD (separate responsibilities)
class ReportGenerator:
    def generate(self):
        print("Generating report")

class ReportSaver:
    def save(self):
        print("Saving report")

rg = ReportGenerator()
rs = ReportSaver()

rg.generate()
rs.save()