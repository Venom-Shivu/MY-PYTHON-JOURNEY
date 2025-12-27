# Default Arguements:
#       We can provide a default value to an argument. This value will be used if the function is called without
#       passing a value for that argument.

def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

print("\n--- Calling function with default argument ---")
greet_with_default("Alice")  # Uses "Alice"
greet_with_default()         # Uses default "Guest" , if the value(name) is not provided.

def multiply(a, b=1):
    print(f"The product of {a} and {b} is {a * b}")

print("\n--- Calling function with a default argument (multiply) ---")
multiply(10, 5) # b will be 5
multiply(7)     # b will be 1 (default value)


# Keyword Arguements:
#       We can call a function with keyword arguments. This means we specify the argument name along with its value.

def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

print("\n--- Calling function with keyword arguments ---")
describe_person(name="Bob", age=30, city="New York")
describe_person(city="London", name="Charlie", age=25) # Order doesn't matter with keyword arguments


# Keyword-length arguments (**kwargs):
#       Allows a function to accept an arbitrary number of keyword arguments.

# Defines a function named display_info
def display_info(**kwargs):          # **kwargs collects all keyword arguments into a dictionary
    print("\n--- Displaying Info ---")  # Prints a header line for clarity
    for key, value in kwargs.items():  # Loops through each key-value pair in the dictionary
        print(f"{key}: {value}")       # Prints each key and its corresponding value

display_info(name="Alice", age=30, city="New York")  
# Calls the function and passes keyword arguments (stored as a dict in kwargs)

display_info(product="Laptop", price=1200, brand="Dell", quantity=1)  
# Calls the same function with different keyword arguments


# Arbitrary Arguments (*args):
# Variable-length arguments (*args):
#       Allows a function to accept an arbitrary number of positional arguments.

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    print(f"The sum of all numbers is: {total}")

print("\n--- Calling function with variable-length arguments (*args) ---")
sum_all(1, 2, 3)
sum_all(10, 20, 30, 40, 50)



# Required Arguements:
#         The Arguemnts which are necessary to perform an action , without these arguement there would be typerror.
def add(a, b):
    print(f"The sum of {a} and {b} is {a + b}")

print("\n--- Calling function with required arguments ---")
add(5, 3)
# add(5) # This would raise a TypeError because 'b' is a required argument and is missing 




