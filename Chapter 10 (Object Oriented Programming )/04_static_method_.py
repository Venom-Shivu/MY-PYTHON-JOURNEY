# ============================================================
#                   STATIC METHODS (@staticmethod)
# ============================================================
"""
    CONCEPT:    A Static Method is a method that belongs to the Class rather than a specific Object.

Key Differences:
1. It does NOT use the 'self' parameter.
2. It cannot access instance attributes (like self.name).
3. It is marked with the @staticmethod decorator.
4. It is used for utility tasks that don't depend on object state.
"""

class Student:
    school = "Kendriya Vidyalaya" # Class Attribute

    def set_details(self, name, grade):
        # Instance Method: Uses 'self' to store data for this specific student
        self.name = name
        self.grade = grade

    def get_details(self):
        # Instance Method: Uses 'self' to access data
        print(f"Student: {self.name}, Grade: {self.grade}")

    # --------------------------------------------------------
    # STATIC METHOD: General Utility
    # --------------------------------------------------------
    @staticmethod
    def greet_user():
        # This method doesn't care which student calls it.
        # It just prints a generic welcome message.
        # Notice there is NO 'self' in the parentheses.
        print("Welcome to the Student Management System!")

    # --------------------------------------------------------
    # STATIC METHOD: Calculation / Logic
    # --------------------------------------------------------
    @staticmethod
    def check_eligibility(age):
        # This method performs a check based on the input 'age'.
        # It is independent of any specific student object.
        if age >= 6:
            print(f"Age {age}: Eligible for admission.")
        else:
            print(f"Age {age}: Too young for admission.")


# ------------------------------------------------------------
# Using the Static Methods
# ------------------------------------------------------------

print("--- Calling Static Methods (No Object needed) ---")
# We can call static methods directly using the Class name (Preferred way)
Student.greet_user()
Student.check_eligibility(5)
Student.check_eligibility(8)

print("\n--- Using Instance Methods (Object needed) ---")
# Creating an object to show the difference
s1 = Student()
s1.set_details("Arjun", 9)
s1.get_details()

# You can also call a static method from an object, but it's effectively the same as calling it from the Class
print("\n(Calling static method via object s1):")
s1.greet_user()