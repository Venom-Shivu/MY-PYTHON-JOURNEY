"""
=====================================================
                LIST COMPREHENSIONS IN PYTHON
=====================================================

What is a list comprehension?
- A compact way to create lists
- Replaces verbose for-loops + append()
- Improves readability and reduces boilerplate code

General Syntax:
    new_list = [expression for item in iterable if condition]
"""

# ---------------------------------------------------
# Base list used in all examples
# ---------------------------------------------------
numbers = [1, 6, 12, 7, 11, 33]

print("\n========== EXAMPLE 1 : TRADITIONAL WAY (NOT RECOMMENDED) ==========")

# Old-style approach using loop + append
squared_traditional = []

for num in numbers:
    squared_traditional.append(num * num)

print(f"Original List : {numbers}")
print(f"Squared List  : {squared_traditional}")


print("\n========== EXAMPLE 2 : LIST COMPREHENSION (CORRECT WAY) ==========")

# Same result using list comprehension
squared_comp = [num * num for num in numbers]

print(f"Original List : {numbers}")
print(f"Squared List  : {squared_comp}")


print("\n========== EXAMPLE 3 : LIST COMPREHENSION WITH CONDITION ==========")

# Square only even numbers
even_squares = [num * num for num in numbers if num % 2 == 0]

print("Even numbers squared:")
print(even_squares)


print("\n========== EXAMPLE 4 : TRANSFORMING DATA ==========")

# Convert numbers to strings with labels
labeled_numbers = [f"Value = {num}" for num in numbers]

print("Labeled values:")
print(labeled_numbers)


print("\n========== EXAMPLE 5 : LIST COMPREHENSION ON STRINGS ==========")

name = "PYTHON"

# Convert each character to lowercase
lower_chars = [char.lower() for char in name]

print(f"Original String : {name}")
print(f"Lowercase chars : {lower_chars}")


print("\n========== EXAMPLE 6 : CONDITIONAL EXPRESSION INSIDE COMPREHENSION ==========")

# Tag numbers as Even or Odd
even_odd_tags = ["Even" if num % 2 == 0 else "Odd" for num in numbers]

print("Even / Odd classification:")
print(even_odd_tags)


print("\n========== EXAMPLE 7 : NESTED LIST COMPREHENSION ==========")

# Create pairs (number, square)
number_square_pairs = [(num, num * num) for num in numbers]

print("Number and its square:")
print(number_square_pairs)


print("\n========== EXAMPLE 8 : REALISTIC USE CASE ==========")

# Filter valid marks (ignore invalid ones)
marks = [95, 82, -1, 67, 101, 88]

valid_marks = [mark for mark in marks if 0 <= mark <= 100]

print(f"All marks   : {marks}")
print(f"Valid marks : {valid_marks}")


print("\n========== COMPARISON SUMMARY ==========")

print("❌ for-loop + append → more lines, more mistakes")
print("✅ list comprehension → concise, readable, Pythonic")

print("\n========== END OF LIST COMPREHENSION DEMO ==========")
