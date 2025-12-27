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
    # Class Attributes
    # These are variables that belong to the class itself.
    # All objects created from this class will share these initial values.
    name = "Rohan"
    occupation = "Software Developer"
    net_worth = 100000

# ============================================================
#                       OBJECT
# ============================================================

# An object is an instance of a class.
# Memory is allocated only when the object is created.

# Creating an object (Instance)
shiva = Employee() 
# shiva is now an object of class Employee.

# Accessing Class Attributes via Object
print("-------Default values from Class Attributes:--------")
print(shiva.name)
print(shiva.occupation)
print(shiva.net_worth)

# Creating Instance Attributes
# We can modify the attributes for this specific object
shiva.name = "Shiva"
shiva.occupation = "Data Scientist"
shiva.net_worth = 120000

print("\n------After creating Instance Attributes:-------")
print(shiva.name)
print(shiva.occupation)
print(shiva.net_worth)

# Creating another object
divya = Employee()
divya.name = "Divya"
divya.occupation = "HR"
divya.net_worth = 500000

print("\n-------Second Object (Divya):---------")
print(divya.name) 
print(divya.occupation)
print(divya.net_worth)

# The __dict__ attribute returns a dictionary containing the object's instance attributes.
print("\n-----------Dictionary of instance attributes for shiva:---------")
print(shiva.__dict__) 


# ============================================================
#           MODELING A PROBLEM USING OOP
# ============================================================

"""
Step-by-step thinking process:

1. Identify NOUNS       → Classes
2. Identify ADJECTIVES  → Attributes
3. Identify VERBS       → Methods (To be covered later)

Example:
NOUN        → Employee
ADJECTIVES  → name, occupation, net_worth
"""
