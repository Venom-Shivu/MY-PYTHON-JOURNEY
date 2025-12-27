# Write a recursive function to calculate the sum of first n natural numbers.

"""
sum (1) = 1
sum (2) = 1 + 2
sum (3) = 1 + 2 + 3
sum (4) = 1 + 2 + 3 + 4
sum (5) = 1 + 2 + 3 + 4 + 5

sum (n) =  1 + 2 + 3 + 4 + 5 +............+ (n-1) + n
sum (n) = sum (n-1) + n
"""

# renamed to 'calculate_sum' to avoid overriding the built-in 'sum()' function in python as we are defining the function by self
def calculate_sum(n):
    # --- BASE CONDITION ---
    # This is the 'Stop' signal. 
    # We know the sum of the first 1 natural number is just 1.
    # If we don't have this, n will become 0, -1, -2... forever.
    if n == 1:
        return 1
    # --- RECURSIVE STEP ---
    # If n is not 1, we haven't reached the end yet.
    # Keep calling the function with a smaller number.
    return calculate_sum(n - 1) + n # It is calcultaed as sum(5) = 5 + Sum(4) and so on

# Adding a check for 0 or negative numbers just in case
try:
    n = int(input("Enter the Number: "))
    if n <= 0:
        print("Please enter a positive integer.") # This checks if the number is 0 ir negative and returns error message
    else:
        result = calculate_sum(n) # if the number is positive then it moves to the else case and result is printed
        print(f"The sum of first {n} natural numbers is {result}")
except ValueError:
    print("Invalid input! Please enter a number.") # this handles if the input is other than integer and returns the error to user.
