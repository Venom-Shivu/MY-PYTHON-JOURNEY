"""
Write a program to print the following star pattern:
*
**
***  For n = 3
"""
# taking the input from the user as integer
n = int(input("Enter the number: "))
# To execute the loop for n number of lines we take (1 to n+1) to go upto n as for loop runs to (n-1) for n
for i in range(1,n+1):
# To print the star i times we simply print stars starting from i = 1 to i = n no pattern is specified, stars will be 1 star in first line, 2 in second..
    print("*"*i, end = "")
# To print a new empty line we use the empty print statement
    print("")
