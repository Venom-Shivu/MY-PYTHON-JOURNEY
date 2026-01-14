"""
Problem Statement:
    Write a Python program that generates the multiplication table (1 to 10)
    for a user-entered integer using a list comprehension.
    The table must be:
      1. Displayed on the console in a readable format, and
      2. Stored in a text file named "multiplication_tables.txt",
         with the table clearly labeled by the corresponding number.
"""

# Read integer input from the user
number = int(input("Enter an integer to generate its multiplication table: "))

# Generate formatted multiplication table using list comprehension
multiplication_table = [
    f"{number} x {i} = {number * i}"
    for i in range(1, 11)
]

# Display the table on the console
print(f"\nMultiplication Table for {number}")
print("-" * 30)
for line in multiplication_table:
    print(line)

# Store the table in a text file (append mode allows multiple tables)
with open("multiplication_tables.txt", "a") as file:
    file.write(f"\nMultiplication Table for {number}\n")
    file.write("-" * 30 + "\n")
    for line in multiplication_table:
        file.write(line + "\n")

print("\nTable successfully displayed and saved to 'multiplication_tables.txt'")
