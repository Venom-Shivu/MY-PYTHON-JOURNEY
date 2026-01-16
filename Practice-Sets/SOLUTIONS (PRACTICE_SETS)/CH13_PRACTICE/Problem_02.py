"""
Write a Python program that accepts a student’s name, ranking, percentage score, and phone number as input.
The program must validate the inputs such that:
->The percentage score must be between 0 and 100 (inclusive).
->The phone number must contain exactly 10 numeric digits.

If any input violates these constraints, the program should display an appropriate error message and terminate execution.

Upon successful validation, display the details using the str.format() method in the following format:

The name of the developer is <Name>, he got a ranking of <Rank> with <Percentage>% in the Coding Competition.
The registered contact number of the developer is <Phone Number>."
 
"""
# ------------------------------------------------------------
# Program: Student Details Formatter with Input Validation
# ------------------------------------------------------------

name = input("Enter student name: ")
rank = int(input("Enter ranking: "))

percentage = float(input("Enter percentage score (0–100): "))
if percentage < 0 or percentage > 100:
    print("Error: Percentage must be between 0 and 100.")
    exit()

phone = input("Enter phone number (10 digits): ")
if len(phone) != 10 or not phone.isdigit():
    print("Error: Phone number must contain exactly 10 digits.")
    exit()

# Formatted output using format() method
output = (
    "The name of the developer is {}, he got a ranking of {} with {}% in the Coding Competition.\n"
    "The registered contact number of the developer is {}."
).format(name, rank, percentage, phone)

print(output)
