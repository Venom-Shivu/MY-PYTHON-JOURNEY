"""                         TYPES OF FUNCTIONS
 There are two types of functions in Python:

 1. Built-in functions:
    Example: print(), len(), type(), input(), range(), etc.
    =>These are pre-defined functions that are always available for use.
    =>These are already present in Python.

 2. User-defined functions
    => These are functions created by the user to perform specific tasks/jobs.
    => These functions are defined by the user as per their requirements.
 """

# Function With Arguement:
#       A function can accept some value it can work with. We can put these values in the parantheses.
#       A function can also return value as shown below:


def grt(name, ending): # the ending will be printed next to the greet message.
    print("Hello! " + name)
    print(ending)
    return "OK"
'''The return statement immediately stops the execution of a function and sends a value (or object) back to the place 
where the function was called. This returned value is then typically assigned to a variable or used directly in an 
expression by the calling code.'''
a = grt("Shivansh", "Welcome to Python Programming.")
print(a) 
grt("Shivam", "Welcome to Python Coding.")
grt("Shubhankar", "Welcome to the World of Programming.")

# Function Without Arguement:
def no_arg_func():
    print("This function takes no arguments.")
    print("It just prints a message.")
    return "No arguments here!"
print("\n--- Calling function without arguments ---")
b = no_arg_func()
print(b)

