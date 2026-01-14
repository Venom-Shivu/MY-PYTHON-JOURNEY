"""
Problem Statement:
Write a Python program that iterates over a list using the enumerate() function and prints
the elements located at the 3rd, 5th, and 7th positions. The solution must rely on index 
tracking provided by enumerate() rather than direct indexing.
"""

# Input data
numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]

# Target positions to be displayed (1-based indexing)
target_positions = {3, 5, 7}

for index, value in enumerate(numbers, start=1):
    # Check if the current position is one of the required positions
    if index in target_positions:
        print(f"Element at position {index}: {value}")
