# Write a program using functions to find the greatest of three numbers.

a = int(input("Enter Your Number: "))
    # Takes the first number as input from the user.
b = int(input("Enter Your Number: "))
    # Takes the second number as input from the user.
c = int(input("Enter Your Number: "))
    # Takes the third number as input from the user.
def greatest(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c # This criteria tells that if a>b and a>c then a is greater else c is greater
    else:
        if b > c:
            return b
        else:
            return c # This criteria tells that if b>c then b is greater else c is greater
        
result = greatest(a, b, c) # result stores the function call  in a variable
print(f"The Greatest of the three is: {result}")