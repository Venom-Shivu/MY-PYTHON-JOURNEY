#       ====================================
#               MULTIPLE INHERITANCE
#       ====================================

"""
MULTIPLE INHERITANCE IN PYTHON
==============================

DEFINITION:
Multiple Inheritance occurs when a child class inherits from MORE THAN ONE parent class.

SYNTAX:
class Child(Parent1, Parent2):
    pass

KEY POINTS:
1. The child class gets access to attributes and methods of ALL parent classes.
2. If multiple parents have the SAME attribute or method name,
   Python resolves the conflict using MRO (Method Resolution Order).
3. MRO follows LEFT-TO-RIGHT order as written in the class definition.
"""

# --------------------------------------------------
# Parent Class 1
# --------------------------------------------------
class Employee:
    """
    Represents an employee working for a company.
    """
    company = "Visa"          # Class attribute
    employee_code = 120       # Class attribute


# --------------------------------------------------
# Parent Class 2
# --------------------------------------------------
class Freelancer:
    """
    Represents a freelancer working independently.
    """
    company = "Fiverr"        # Same attribute name as Employee (conflict case)
    level = 0                # Freelancer level

    def upgrade_level(self):
        """
        Increases freelancer level by 1.
        """
        self.level += 1


# --------------------------------------------------
# Child Class (Multiple Inheritance)
# --------------------------------------------------
class Programmer(Employee, Freelancer):
    """
    Programmer inherits from BOTH Employee and Freelancer.

    MRO (Method Resolution Order):
    Programmer -> Employee -> Freelancer -> object
    """
    name = "Rohit"


# --------------------------------------------------
# Object Creation & Usage
# --------------------------------------------------
p = Programmer()

# Accessing attribute from Employee
print(f"Employee Code  : {p.employee_code}")  # Output: 120

# Accessing method and attribute from Freelancer
p.upgrade_level()
print(f"Freelancer Lvl : {p.level}")           # Output: 1

# --------------------------------------------------
# ATTRIBUTE CONFLICT RESOLUTION (IMPORTANT)
# --------------------------------------------------
# Both Employee and Freelancer define `company`
# Python follows MRO:
# Programmer -> Employee -> Freelancer
# Hence, Employee.company is chosen

print(f"Company Name   : {p.company}")         # Output: Visa

# Optional: View the Method Resolution Order
print(Programmer.mro())
 # Output: (<class '__main__.Programmer'>, <class '__main__.Employee'>, <class '__main__.Freelancer'>, <class 'object'>)
