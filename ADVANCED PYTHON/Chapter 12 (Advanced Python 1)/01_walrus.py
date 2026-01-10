"""
WALRUS OPERATOR (:=) — Assignment Expression

Introduced in Python 3.8, the walrus operator allows you to:
- Assign a value to a variable
- Use that value immediately within an expression

Syntax:
    variable := expression

Use it ONLY when it improves clarity.
Do NOT use it just to look smart.
"""

# ---------------------------------------------------
# Example 1: Basic  Use Case
# ---------------------------------------------------

name = "Shivansh Yadav"

# Assign length and compare in a single expression
if (length := len(name)) > 10:
    print(f"Length is {length}, which is greater than 10")
else:
    print(f"Length is {length}, which is 10 or less")


# ---------------------------------------------------
# Example 2: Without Walrus Operator (for comparison)
# ---------------------------------------------------
# This is what we used to do before Python 3.8

length = len(name)

if length > 10:
    print(f"Length is {length}, which is greater than 10")
else:
    print(f"Length is {length}, which is 10 or less")


# ---------------------------------------------------
# Example 3: Walrus Operator in Loops
# ---------------------------------------------------
# Useful when a value is needed both for checking
# and for processing inside the loop

numbers = [5, 12, 3, 20, 7]

# Print numbers only if their square is greater than 100
for num in numbers:
    if (square := num ** 2) > 100:
        print(f"{num} squared is {square}")


# ---------------------------------------------------
# Example 4: List Comprehension (Use Carefully)
# ---------------------------------------------------
# Walrus can improve performance, but readability matters

values = ["10", "20", "abc", "30"]

# Convert only valid numeric strings to integers
numbers = [num for val in values if (num := val).isdigit()]

print(f"The list is: {numbers}")


# ---------------------------------------------------
# Example 5: Input Validation (Very Common Use Case)
# ---------------------------------------------------

# Read input and validate in one line
while (user_input := input("Enter a number (type 'q' to quit): ")) != "q":
    print(f"You entered: {user_input}")