"""
_______________RECURSION_____________
                     It is a function which calls itself.
                    It is used to directly use a mathematical formula as a function.

Step        |    Mathematical Logic        |      Description
Base Case   |        1!=1                  |      The simplest case. No more calls needed.
Step 2      |    2!=2 X 1!=2 X 1=2         |      Calls factorial(1) and multiplies by 2.
Step 3      |    3!=3 X 2!=3 X 2=6         |      Calls factorial(2) and multiplies by 3.
Step 4      |    4!=4 X 3!=4 X 6=24        |      Calls factorial(3) and multiplies by 4.
Step 5      |    5!=5 X 4!=5 X 24=120      |      Calls factorial(4) and multiplies by 5.

This concludes that the factorial calls the factorial of previous number as a reference and multilply it with the number given fr factorial.               

Example:
factorial(n) = n X factorial (n-1) X ......... 3 X 2 X 1

"""
def factorial(n):
    if n == 0 or n == 1: # this is base condition which doesn't call the function any further
        return 1
    else:
       return n*factorial(n-1) # function calling itself

n = int(input("Enter a Number to find it's factorial: ")) # This takes input from the user.
result = factorial(n) # Result stores the value of the function call i.e., factorial(n)
print(f"The Factorial of {n} is {result}")
      

"""
This work as follows:

                Factorial (5)
                5 X Factorial (4)
                5 X 4 X Factorial (3)
                5 X 4 X 3 X factorial (2)
                5 X 4 X 3 X 2 X Factorial (1)
                5 X 4 X 3 X 2 X 1 = 120
 
The programmer needs to be extremely carefull while working with  recursion to ensure that the function doesn't infinitely 
keep calling itself. Recusion is sometimes the most direct way to code on algorithm.

"""