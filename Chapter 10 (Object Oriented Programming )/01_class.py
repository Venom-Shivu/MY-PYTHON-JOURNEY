#                       OBJECT ORIENTED PROGRAMMING

'''
    Solving a problem by creating objects is one of the most popular approaches in programming.
    This is called Object Oriented Programming
'''
# This concept focuses on using reusable code (DRY ( Don't Repeat Yourself) Principle )
# Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.

# ============================================================
#                       CLASS
# ============================================================

# A class is a blueprint used to create objects.
# It defines:
#   1. Attributes (data/state)
#   2. Methods (behavior)

"""
Conceptual Flow:

| Blueprint |  ----->  | CLASS |  ----->  | OBJECT (Instance) |
|-----------|          |       |          | Real entity      |

Real-world analogy:
Blank Form  ----->  Filled by User  ----->  Actual Application
(Class)             (Initialization)        (Object)
"""


class Employee:
    """
    Employee represents a real-world employee entity.

    Attributes:
        name (str): Name of the employee
        occupation (str): Job role
        net_worth (int): Financial worth"""
    """
-------EXAMPLE OF A CLASS:-----------
class Employee()
    language = "Python"
    salary = 120000

shivu = Employee()
print(shivu.language, shivu.salary) # Returns Python 120000

""" # This closing triple quote was intended to close the docstring for the class, not the example. This is a class variable.
 #This is an example of a class variable.
 
    def __init__(self, name, occupation, net_worth):
        """
        Constructor method.
        Automatically runs when a new object is created.

        It initializes instance-specific data.
        """
        self.name = name
        self.occupation = occupation
        self.net_worth = net_worth
#                   The `__init__` function
# All classes have a function called `__init__()`, which is always executed when the class is being initiated.
# Use the `__init__()` function to assign values to object properties,
# or other operations that are necessary to do when the object is being created:

    def info(self):
        """
        Displays basic information about the employee.
        """
        print(f"{self.name} works as a {self.occupation} with salary ₹{self.net_worth}.")

# The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.
# It does not have to be named `self`, you can call it whatever you like,
# but it has to be the first parameter of any function in the class.
# The `self` parameter is implicitly passed when you call a method on an object.


# ============================================================
#                       OBJECT
# ============================================================

# An object is an instance of a class.
# Memory is allocated only when the object is created.
# Objects of a given class can invoke the methods available to it without revealing the implementation
# detailed to the user.--ABSTTRACTIONS & ENCAPSULATION! 

#INSTANCE ATTRIBUTES: An attribute that belongs to the instance (object). Assuming the class in previuos example (self.name, self.net_worth and so on)
# NOTE: Instance attributes, take preference over class attributes during assignment and retrieval.


a = Employee("Shiva", "Programmer", '10,00,000') # To use comma in salary it is now in string format not number format (int)
b = Employee("Divya", "HR", 500_000)
c = Employee("Rahul", "Accountant", 700_000)
d = Employee("Venom", "Data-Analyst",150000)

# Accessing instance attributes
print(a.name)

print(a.occupation)
print(a.net_worth)
# Calling methods on objects
a.info()
print(b.name)
print(b.net_worth)
print(b.__dict__) # The __dict__ attribute returns a dictionary containing the object's instance attributes. This is an instance dictionary.
print(b.occupation)
b.info()
c.info()
d.info()

print(a.__dict__) 


# ============================================================
#           MODELING A PROBLEM USING OOP
# ============================================================

"""
Step-by-step thinking process:

1. Identify NOUNS       → Classes
2. Identify ADJECTIVES  → Attributes
3. Identify VERBS       → Methods

Example:
NOUN        → Employee
ADJECTIVES  → name, occupation, net_worth
VERBS       → info(), increment_salary(), get_salary()
"""
