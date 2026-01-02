# Write a program to calculate the factorial of a given number using for loop

# Taking the input from the user
input_number = int(input("Enter your Number: "))

# Initializing the product from 1.
product = 1
# Start the loop. We need to multiply numbers from 1 up to and including 'input_number'.
# The range goes from 1 to (input_number + 1) because 'range' stops before the end number.
for i in range(1, input_number + 1):
    product = product * i
# In each loop, multiply the current 'product' by the current number 'i'.
    # Example (if input is 5):
    # i=1: product = 1 * 1 = 1
    # i=2: product = 1 * 2 = 2
    # i=3: product = 2 * 3 = 6
    # i=4: product = 6 * 4 = 24
    # i=5: product = 24 * 5 = 120
print(f"The factorial of {input_number} is {product}")   
