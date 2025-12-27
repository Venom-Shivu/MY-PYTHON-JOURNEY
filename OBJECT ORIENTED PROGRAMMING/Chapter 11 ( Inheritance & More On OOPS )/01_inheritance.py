# ============================================================
#                     INHERITANCE IN PYTHON
# ============================================================
"""
INHERITANCE allows a child class to reuse, extend, or override
the behavior of a parent class.

WHY IT MATTERS:
- Avoids code duplication
- Improves maintainability
- Models real-world "IS-A" relationships
  (A Programmer IS an Employee)
"""

# ------------------------------------------------------------
# PARENT CLASS (BASE CLASS)
# ------------------------------------------------------------
class Employee:
    company = "Google"  # Class attribute (shared by all employees)

    def __init__(self, name, age, salary):
        # Common properties for all employees
        self.name = name
        self.age = age
        self.salary = salary

    def show(self):
        # Common behavior for all employees
        print("---- Employee Details ----")
        print(f"Company : {self.company}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Salary  : {self.salary}")


# ------------------------------------------------------------
# CHILD CLASS (DERIVED CLASS)
# ------------------------------------------------------------
class Programmer(Employee):
    company = "Microsoft"  # Overrides parent class attribute

    def __init__(self, name, age, salary, language, experience):
        # Call parent constructor to initialize shared attributes
        
        super().__init__(name, age, salary)
        # Calls the constructor of the parent class (Employee)
        # to initialize common attributes (name, age, salary).
        # Without this, the child object would NOT have these attributes,
        # and inherited methods like show() would raise AttributeError.


        # Programmer-specific properties
        self.language = language
        self.experience = experience

    def show_language(self):
        # Behavior unique to Programmer
        print("---- Programmer Skills ----")
        print(f"Language   : {self.language}")
        print(f"Experience : {self.experience} years")


# ------------------------------------------------------------
# OBJECT CREATION & USAGE
# ------------------------------------------------------------
# Creating an Employee object
emp = Employee("Rahul", 30, 70000)

# Creating a Programmer object (inherits from Employee)
prog = Programmer("Shivansh", 22, 90000, "Python", 2)

# ------------------------------------------------------------
# DEMONSTRATION
# ------------------------------------------------------------
emp.show()          # Uses Employee's method
print()

prog.show()         # Inherited method from Employee
prog.show_language()  # Programmer's own method
