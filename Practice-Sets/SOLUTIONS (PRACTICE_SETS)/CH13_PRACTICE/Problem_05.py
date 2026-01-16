"""

Write a Python program to determine the maximum value in a list of integers using the 
reduce() function from the functools module.

Implement the solution in two ways:

1. By finding the maximum value from a predefined list of integers.
2. By finding the maximum value from a list of integers provided by the user at runtime.
"""

from functools import reduce

#===========================
#--------METHOD 1-----------
#===========================

# Predefined list of numbers
numbers = [23, 45, 12, 89, 34, 67]

# Using reduce to find the maximum value
maximum_value = reduce(lambda a, b: a if a > b else b, numbers)

print("========== METHOD 1 : PREDEFINED LIST ==========")
print(f"Maximum value: {maximum_value}\n")


#===========================
#--------METHOD 2-----------
#===========================

# Taking list input from the user
print("========== METHOD 2 : USER INPUT ==========")
user_numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Using reduce to find the maximum value
maximum_value = reduce(lambda a, b: a if a > b else b, user_numbers)

print("Maximum value:", maximum_value)
