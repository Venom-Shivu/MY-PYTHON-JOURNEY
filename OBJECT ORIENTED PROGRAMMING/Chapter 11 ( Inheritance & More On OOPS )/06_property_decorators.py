# ============================================================
#        PROPERTY DECORATORS (GETTERS / SETTERS)
# ============================================================

"""
PROPERTY DECORATORS:
--------------------
Property decorators allow methods to be accessed like attributes.

WHY WE USE THEM:
1. To protect internal data (encapsulation)
2. To validate or control values before setting them
3. To compute values dynamically instead of storing them

MAIN DECORATORS:
- @property              -> Getter (read-only access)
- @property_name.setter  -> Setter (controlled write access)
"""

class Employee:
    # --------------------------------------------------------
    # CLASS ATTRIBUTE
    # --------------------------------------------------------
    # Shared by ALL objects of the class
    company = "Venom Corp"

    def __init__(self, first_name, last_name):
        # INSTANCE ATTRIBUTES
        # Unique for each object
        self.first_name = first_name
        self.last_name = last_name

    # --------------------------------------------------------
    # CLASS METHOD
    # --------------------------------------------------------
    @classmethod
    def show_company(cls):
        # 'cls' refers to the class itself, not an object
        print(f"Company Name: {cls.company}")

    # --------------------------------------------------------
    # GETTER (READ ACCESS)
    # --------------------------------------------------------
    @property
    def name(self):
        """
        Acts like an attribute but is actually a method.
        Combines first_name and last_name dynamically.
        """
        return f"{self.first_name} {self.last_name}"

    # --------------------------------------------------------
    # SETTER (WRITE ACCESS)
    # --------------------------------------------------------
    @name.setter
    def name(self, value):
        """
        Controls how 'name' is assigned.
        Ensures proper splitting of first and last name.
        """
       
        # 'parts' is a list created from the split() operation.
        # Example: "Shivansh Yadav".split(" ") → ["Shivansh", "Yadav"]
        parts = value.split(" ")


        if len(parts) != 2:
            raise ValueError("Name must contain exactly two words")

        # parts[0] accesses the FIRST element of the list → first name
        self.first_name = parts[0]

        # parts[1] accesses the SECOND element of the list → last name
        self.last_name = parts[1]


# ============================================================
#                OBJECT CREATION & USAGE
# ============================================================

# Creating an object (instance)
emp = Employee("Venom", "Shivansh")

# Accessing property (getter)
print(emp.name)   # Looks like an attribute, works like a method

# Modifying property (setter)
emp.name = "Shivansh Yadav"

# Accessing updated instance attributes
print(emp.first_name)
print(emp.last_name)

# Accessing class method
Employee.show_company()
