"""
========================================
06_strategy_real_world.py
========================================
Real-world Strategy:

✔ Sorting / filtering logic change
"""

class SortStrategy:
    def sort(self, data):
        pass

class AscendingSort(SortStrategy):
    def sort(self, data):
        return sorted(data)

class DescendingSort(SortStrategy):
    def sort(self, data):
        return sorted(data, reverse=True)

class DataProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self, data):
        return self.strategy.sort(data)

data = [5, 2, 9, 1]

processor = DataProcessor(AscendingSort())
print(processor.process(data))

processor.strategy = DescendingSort()
print(processor.process(data))