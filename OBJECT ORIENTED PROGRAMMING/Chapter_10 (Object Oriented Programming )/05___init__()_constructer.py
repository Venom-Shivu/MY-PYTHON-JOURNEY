#                           ==================================================
#                                    __init__() CONSTRUCTOR & "DUNDER"
#                           ==================================================

# A "dunder" method means:
'''         Double UNDERscore method → __something__
            These methods are special and are called by Python automatically.
            Example: __init__, __str__, __len__       '''

# __init__ is a dunder method used to SET UP an object.
# Think of it as "object setup" or "object birth method".
# It is also called a CONSTRUCTOR.

class Employee:

    # __init__ runs automatically when a new object is created
    # It is used to give initial values to the object
    def __init__(self, name, salary, language):
       
        # self refers to the current object being created
        # We store data inside the object using self.variable
        self.name = name
        self.salary = salary
        self.language = language


    # Normal method (not a dunder method)
    # This method only runs when we call it manually
    def get_details(self):
        print(f"---------Initializing Employee Object with __init__ for {self.name}---------")
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Language:", self.language)
        print("-" * 20)


# ============================================================
# Object Creation
# ============================================================

# When we write Employee(...):
# 1. Python creates a new empty object
# 2. Python automatically calls __init__() after object is created
# 3. Data is stored inside the object

shivu = Employee("Shiva", 120000, "Python")
rohan = Employee("Rohan", 50000, "Java")

# Calling normal methods using the object
shivu.get_details()
rohan.get_details()
