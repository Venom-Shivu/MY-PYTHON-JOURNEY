# Write a program to print multiplication table of a given number using for loop.

input_number = int(input("Enter a number to print its multiplication table: "))

for i in range(1, 11):
 
    print(f"{input_number} x {i} = {input_number * i}")

# Explaination:
# {for i in range(1, 11):} is used to iterate through numbers 1 to 10 (the multipliers for the multiplication table)
# {input_number} is the input number for which we want to print the multiplication table.
