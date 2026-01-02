# Write a program to find the sum of first n natural numbers using While Loop

number = int(input("Enter the Number: "))
# Initialize the 'sum' variable to 0. This variable will store the running total.
i = 1
# Initialize the 'sum' variable to 0. This variable will store the running total.
sum = 0
# Start the while loop. It will continue as long as the counter 'i' is less than or equal to 'number'.
while(i <= number):

# Add the current value of the counter 'i' to the 'sum' variable.
# (This is equivalent to: sum = sum + i)
    sum += i

# Increase the counter 'i' by 1 to move to the next natural number.
 # (This is equivalent to: i = i + 1)
    i += 1
# After the loop finishes (i.e., when i becomes greater than 'number'), 
# print the final calculated sum.
print(sum)