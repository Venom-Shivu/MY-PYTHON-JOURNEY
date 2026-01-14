"""
Problem Statement:
    Write a Python program that uses a list comprehension to generate
    the multiplication table (from 1 to 10) for a user-entered integer.
    Each entry in the list must be a formatted string in the form:
        "<number> x <multiplier> = <result>"
"""

# Read integer input from the user
number = int(input("Enter an integer to generate its multiplication table: "))

# Generate formatted multiplication table using list comprehension
multiplication_table = [
    f"{number} x {i} = {number * i}"
    for i in range(1, 11)
]

# Display the result
print("\nMultiplication Table:")
print(multiplication_table)
