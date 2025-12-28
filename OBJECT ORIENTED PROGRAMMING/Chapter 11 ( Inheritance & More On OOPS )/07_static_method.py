# ============================================================
#                     STATIC METHODS
# ============================================================

"""
STATIC METHOD:
--------------
A static method is a method placed inside a class
ONLY because it logically belongs there.

It does NOT use:
- self  (object data)
- cls   (class data)

It behaves like a normal function, but with class-level grouping.
"""

class Employee:

    # CLASS ATTRIBUTE (shared by all employees)
    company = "Venom Corp"

    def __init__(self, first_name, last_name):
        # INSTANCE ATTRIBUTES (unique to each object)
        self.first_name = first_name
        self.last_name = last_name

    # --------------------------------------------------------
    # STATIC METHOD
    # --------------------------------------------------------
    @staticmethod
    def is_valid_name(name):
        """
        Static method used for validation.
        It does NOT depend on object or class data.
        """
        # Name must contain exactly two words
        parts = name.split(" ")
        return len(parts) == 2

    # --------------------------------------------------------
    # INSTANCE METHOD
    # --------------------------------------------------------
    def show_details(self):
        # Uses instance data, so 'self' is required
        print(f"Employee Name : {self.first_name} {self.last_name}")
        print(f"Company       : {Employee.company}")


# ============================================================
#                 USAGE & DEMONSTRATION
# ============================================================

# Using static method with CLASS name (BEST PRACTICE)
print("Using static method with class name:")
print(Employee.is_valid_name("Venom Shivansh"))   # True
print(Employee.is_valid_name("Venom"))             # False


# Creating an Employee object
emp = Employee("Venom", "Shivansh")

# Calling instance method
emp.show_details()


# ------------------------------------------------------------
# Static method can be called using object (NOT recommended)
# ------------------------------------------------------------
print("\nCalling static method using object (works but bad practice):")
print(emp.is_valid_name("Shivansh Yadav"))
