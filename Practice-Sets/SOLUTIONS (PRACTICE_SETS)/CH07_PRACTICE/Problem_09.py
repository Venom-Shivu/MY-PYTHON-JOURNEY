"""             Write a program to print the following star pattern.

***
* * for n = 3
***                                         """

# taking the input from the user as integer
n = int(input("Enter the Number: "))
# Main loop to run for 'n' number of rows.
# The range goes from 1 up to 'n' (inclusive).
for  i in range(1,n+1):
# Check for the top row (i = 1) OR the bottom row (i = n).
    if (i == 1 or i == n):
# For the first and last rows, print a solid line of 'n' stars.
        print("*"* n, end = "")
# If the lines are not first and last these are lines in between we form a ring of stars.. 1at start and one at last
    else:
# 1. Print the starting star for the row.
        print("*", end = "")
# 2. Print the required spaces between the two stars.
        # The space needed is the total width (n) minus the two stars at the ends (n - 2).
        # Example (n=3): 3 - 2 = 1 space.
        print(" "*(n-2), end = "")
# 3. Print the ending star for the row.
        print("*", end = "")
# After finishing the output for the current row use an empty print statement to move the cursor to the next line.
    print("")