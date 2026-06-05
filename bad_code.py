# bad_code.py
def calculate_total(items):
    total = 0
    for item in items:
        # This code is missing error handling and optimization
        total = total + item['price']
    return total

# This script has no docstring, no type hints, and is prone to errors.