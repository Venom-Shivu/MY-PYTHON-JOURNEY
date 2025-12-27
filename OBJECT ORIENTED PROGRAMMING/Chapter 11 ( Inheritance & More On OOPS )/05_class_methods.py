# ============================================================
#                       CLASS METHODS
# ============================================================
"""
WHAT IS A CLASS METHOD?
-----------------------
A class method works with the CLASS itself, not with a
specific object (instance).

Key points:
1. It uses the @classmethod decorator
2. It receives the class as the first argument (cls)
3. It can access and modify class variables
4. It is shared across all objects of the class
"""

class Employee:
    # Class variable (belongs to the class, not to any object)
    a = 1

    @classmethod
    def show(cls):
        # cls represents the CLASS (Employee), not an instance.
        # Using 'self' here would be misleading because:
        # 1. No object is involved in a class method
        # 2. The method works on class-level data
        # 3. 'self' implies instance-specific behavior, which is false here
        # Python allows 'self', but using it is poor practice and confuses readers
        print(f"The class value of a is {cls.a}")


# ============================================================
#                   INSTANCE VS CLASS
# ============================================================

e = Employee()

# Creates an INSTANCE variable 'a' for this object only
e.a = 40

# Class method always refers to the CLASS variable
print("Calling class method using class name:")
Employee.show()   # Output: 1
print("\nCalling class method using object:")
e.show()          # Output: 1

