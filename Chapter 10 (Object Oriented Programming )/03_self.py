# ============================================================
#                   THE 'SELF' PARAMETER
# ============================================================

"""
CONCEPT:
The 'self' parameter is a reference to the current instance of the class.
It is used to access variables (attributes) that belong to the specific object.

Why do we need it?
When you create multiple objects (e.g., obj1, obj2), the method needs to know 
WHICH object's data to use. 'self' tells the method "use the data of the object that called me".
"""

class Employee:
    language = "Python" # Class Attribute
    salary = 120000     # Class Attribute
  
    def getDetails(self):
        """Method to print employee details."""
        # self.name accesses the 'name' attribute of the specific object invoking this method
        print(f"The Name of Employee is {self.name} and programming language is {self.language}.")
        print(f"The Salary of {self.name} is {self.salary}.")

    def greet(self):
        """Method to greet the employee."""
        print(f"Hello, {self.name}! Welcome to the office.")

# ------------------------------------------------------------
# Example 1: Using the Employee Class
# ------------------------------------------------------------

shivu = Employee()
shivu.name = "Shiva"      # Instance Attribute
shivu.language = "MySQL"  # Instance Attribute
shivu.salary = 150000     # Instance Attribute

print("--- Example 1: Employee ---")
# Calling the method using the object
shivu.greet()
shivu.getDetails() 

# HOW IT WORKS INTERNALLY:
# shivu.getDetails() is interpreted by Python as: Employee.getDetails(shivu)
# The object 'shivu' is passed automatically to the 'self' argument.

print("\n(Calling via Class name to demonstrate 'self' passing):")
Employee.getDetails(shivu) 


# ------------------------------------------------------------
# Example 2: A Simple Calculator (Maintaining State)
# ------------------------------------------------------------

# This class acts as a container that holds a number.
# It demonstrates how 'self' helps an object "remember" a value between method calls.
class NumberContainer:
    def set_number(self, num):
        # Storing data in the object using 'self'.
        # self.num creates an attribute 'num' specific to this object.
        self.num = num  
    
    def show_square(self):
        # We can access the previously stored number using 'self.num'.
        sq = self.num * self.num
        print(f"The square of {self.num} is {sq}")

print("\n--- Example 2: NumberContainer ---")
n1 = NumberContainer()
n1.set_number(5)
n1.show_square()

n2 = NumberContainer()
n2.set_number(9)
n2.show_square()


# ------------------------------------------------------------
# Example 3: Student Class (Simple Real-world Example)
# ------------------------------------------------------------

class Student:
    school = "Kendriya Vidyalaya" # Class Attribute (Shared by all students)

    def introduce(self):
        # Using 'self' to access the specific student's name and grade
        print(f"Hi, I am {self.name}.")
        print(f"I study in {self.school} in Class {self.grade}.")

print("\n--- Example 3: Student ---")
student1 = Student()
student1.name = "Aarav"   # Instance Attribute
student1.grade = 10       # Instance Attribute
student1.introduce()

student2 = Student()
student2.name = "Ishita"  # Instance Attribute
student2.grade = 12       # Instance Attribute
student2.introduce()
