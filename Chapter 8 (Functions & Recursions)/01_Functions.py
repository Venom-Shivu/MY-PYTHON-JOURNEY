# A function is a block of code or set of statements designed to do a single, specific job.
# Functions help manage complexity by breaking a large program into smaller, organized, and manageable pieces.
# Functions promote code reuse, meaning you can run the same code block multiple times without rewriting it.

'''
a = int(input("Enter Your Number: "))
b = int(input("Enter Your Number: "))
c = int(input("Enter Your Number: "))

 

average =  (a + b + c) / 3

print(average)

a = int(input("Enter Your Number: "))
b = int(input("Enter Your Number: "))
c = int(input("Enter Your Number: "))

average = (a + b + c) / 3

print(average)

'''

# If we want to do the same average for 50 users or more the number of lines of code will very large.
# To Avoid that large number of lines of code we use Functions.

# Defining a function

def avg():
    a = int(input("Enter Your Number: "))
    b = int(input("Enter Your Number: "))
    c = int(input("Enter Your Number: "))

    average = (a + b + c) / 3
    print(average)
# This function can be called any number of times, anywhere in the program.


# Calling the function
# Whenever we want to call a function , we put the name of the function  followed by the parentheses as follows:
avg()
print("Thank You for finding the average.")
avg()
("Thank you for calculating the average.")
avg()
print("Thank You for finding the average.")
avg() # This will print the "Thank you message after the three average calculations."
avg()


