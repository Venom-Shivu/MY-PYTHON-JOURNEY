"""
=====================================================
        LAMBDA FUNCTIONS vs NORMAL FUNCTIONS
=====================================================

This program clearly shows:
- What output comes from a NORMAL function
- What output comes from a LAMBDA function

The print statements are intentionally descriptive so
there is ZERO confusion while reading the output.
"""

# --------------------------------------------------
# Example 1: NORMAL Function
# --------------------------------------------------

def square_normal(number):
    """Returns the square of a number using a normal function"""
    return number * number

print("=== USING NORMAL FUNCTION ===")
print("Input Number: 5")
print("Output (Square):", square_normal(5))
print()  # blank line for readability


# --------------------------------------------------
# Example 2: LAMBDA Function
# --------------------------------------------------

square_lambda = lambda number: number * number

print("=== USING LAMBDA FUNCTION ===")
print("Input Number: 5")
print("Output (Square):", square_lambda(5))
print()


# --------------------------------------------------
# Example 3: User Input with Lambda
# --------------------------------------------------

user_number = int(input("Enter a number for lambda calculation: "))

print("\n=== LAMBDA FUNCTION WITH USER INPUT ===")
print("Input Number:", user_number)
print("Output (Square):", square_lambda(user_number))
print()


# --------------------------------------------------
# Example 4: Multiple Arguments (Lambda)
# --------------------------------------------------

add_lambda = lambda a, b: a + b

print("=== LAMBDA FUNCTION WITH MULTIPLE ARGUMENTS ===")
print("Inputs: 10 and 20")
print("Output (Addition):", add_lambda(10, 20))
print()


# --------------------------------------------------
# Example 5: Lambda with map()
# --------------------------------------------------

numbers = [1, 2, 3, 4, 5]

print("=== LAMBDA WITH MAP FUNCTION ===")
print("Original List:", numbers)

squared_numbers = list(map(lambda x: x * x, numbers))

print("Operation: Squaring each element using lambda")
print("Result:", squared_numbers)
print()


# --------------------------------------------------
# Example 6: Lambda with filter()
# --------------------------------------------------

print("=== LAMBDA WITH FILTER FUNCTION ===")
print("Original List:", numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Operation: Filtering even numbers using lambda")
print("Result:", even_numbers)
print()


# --------------------------------------------------
# Example 7: Lambda Used for Sorting
# --------------------------------------------------

students = [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 90)
]

print("=== LAMBDA USED FOR SORTING ===")
print("Original Data:", students)

sorted_students = sorted(students, key=lambda student: student[1])

print("Operation: Sorting students by marks using lambda")
print("Result:", sorted_students)
print()


# --------------------------------------------------
# Final Summary (Printed Output)
# --------------------------------------------------

print("=== SUMMARY ===")
print("Normal Function  -> Used for clear, reusable logic")
print("Lambda Function  -> Used for short, one-line operations")
print("Rule Reminder    -> Lambda can have multiple inputs but only ONE expression")
