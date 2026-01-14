"""
Problem Statement:
    Write a Python program that computes the division of two integers (a / b).
    If the denominator is zero, the program must handle the resulting
    ZeroDivisionError gracefully and display the message "Infinite"
    instead of terminating abruptly.
"""

# Read numerator input
a = int(input("Enter the numerator (a): "))

try:
    # Read denominator input
    b = int(input("Enter the denominator (b): "))

    # Perform division (Python raises ZeroDivisionError automatically if b == 0)
    result = a / b
    print(f"Result of {a} / {b} = {result}")

except ZeroDivisionError:
    # Handle division by zero explicitly
    print("Infinite")

