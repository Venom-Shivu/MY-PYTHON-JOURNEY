#       Write a python function to print multiplication table of a given number


def multiplication_table(n):
    # We use a for loop with range(1, 11)
    # range(1, 11) generates numbers from 1 up to 10 (it stops before 11)
    for i in range(1, 11):
        
        # We use an f-string to format the output neatly
        # {n} is the number, {i} is the current multiplier, and {i*n} is the result
        print(f"{n} X {i} = {i*n}")

# --- MAIN PROGRAM ---
# We take user input and convert it to an integer (int)
# Note: Changed variable name to 'num' to avoid conflict with built-in input() function
num = int(input("Enter the number to get its multiplication table: "))

# Call the function with the user's number
# This function prints directly, so we don't need to save the result
multiplication_table(num)

