"""
A list contains the multiplication table of the number 7, represented as integers.
Write a Python program to transform this list into a list of string elements, where each element 
represents the vertical format of the corresponding number, with each table element in a new line.
"""
# Multiplication table of 7 stored as a list
table = [7 * i for i in range(1, 11)]

# Convert numbers to strings
table_as_strings = [str(num) for num in table]

# Print vertically (one number per line)
print("\n".join(table_as_strings))


