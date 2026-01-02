""" Write a program to print the following star pattern 
for n = 3

  *
 ***
*****
for n = 5
    *
   ***
  *****
 *******
*********
"""
# taking the input from the user as integer
n = int(input("Enter the number: "))
# To execute the loop for n number of lines we take (1 to n+1) to go upto n as for loop runs to (n-1) for n
for i in range (1, n+1):
# To print the space for (n-i) times for the first line ,(n=3), there will be 2 spaces in 1st line (3-1)
    print(" "* (n-i),end = "")
# To print the star in odd series we use to print stars as (2*i-1) for first star print (2*1-1)=1 star print then again in second line (2*2-1)= 3 star print
    print("*"* (2*i-1), end = "") # by useing end= "" it doesn't create new line, it just create spaces or no spaces as specified
# To print a new line we created an empty print which insert a new line, because above print statement are working on same line.
    print("")


