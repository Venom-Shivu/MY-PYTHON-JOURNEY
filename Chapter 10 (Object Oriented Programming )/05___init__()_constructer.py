#                           ----------------------------------------------------------
#                                          __init__() CONSTRUCTOR
#                           ----------------------------------------------------------

"""  __INIT__() is a special method which is automatically called when an object is created. It is used to initialize the object's state. 
     It is similar to constructors in other object-oriented languages.

KEY POINTS: 
1.  It is known as the CONSTRUCTOR in Object Oriented Programming.
2.  It is automatically invoked (called) the moment an object is instantiated.
3.  Syntax: def __init__(self, arg1, arg2, ...):
4.  Primary Purpose: To INITIALIZE the object's attributes (variables) with specific values.
5.  The 'self' parameter is required (as usual) to refer to the instance being created. 
"""

class Employee:
    # This is the Constructor
    # It takes arguments to set up the object immediately upon creation
    def __init__(self, name, salary, language):
        print(">> __init__ method called: Creating a new Employee object...") 
        
        # Initializing instance attributes
        # We assign the incoming arguments to self.variable_name
        self.name = name
        self.salary = salary
        self.language = language
        
        print(f"   Employee '{self.name}' created successfully!\n")

    def get_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Language: {self.language}")
        print("-" * 20)

# ============================================================
# Creating Objects (Invoking __init__)
# ============================================================

# When we write Employee(...), Python calls __init__(...) internally.

print("--- 1. Creating 'shivu' ---")
# Arguments "Shiva", 120000, "Python" are passed to name, salary, language in __init__
shivu = Employee("Shiva", 120000, "Python") 

print("--- 2. Creating 'rohan' ---")
rohan = Employee("Rohan", 50000, "Java")

# Accessing the data initialized by __init__
print("--- Checking Details ---")
shivu.get_details()
rohan.get_details()

