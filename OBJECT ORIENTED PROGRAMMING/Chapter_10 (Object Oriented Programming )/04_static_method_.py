# ============================================================
#               STATIC METHODS (@staticmethod)
# ============================================================
# Static methods belong to the class, not to a specific object.
# They do NOT use 'self' and do NOT depend on object data.
# They are mainly used for utility or helper operations.

class Student:

    # Class attribute (shared by all students)
    school = "Kendriya Vidyalaya"

    # -------------------------------
    # Instance Methods (need object)
    # -------------------------------
    def set_details(self, name, grade):
        # Stores data inside this specific student object
        self.name = name
        self.grade = grade

    def get_details(self):
        # Accesses and displays object-specific data
        print(f"Student: {self.name}, Grade: {self.grade}")

    # -------------------------------
    # Static Methods (no object needed)
    # -------------------------------
    @staticmethod
    def greet_user():
        # Generic message not linked to any student
        return "Welcome to the Student Management System!"

    @staticmethod
    def check_eligibility(age):
        # Performs logic based only on input value
        if age >= 6:
            return f"Age {age}: Eligible for admission."
        return f"Age {age}: Too young for admission."


# ============================================================
# Using Static Methods
# ============================================================

# Preferred way: call static methods using the class name
print(Student.greet_user())
print(Student.check_eligibility(5))
print(Student.check_eligibility(8))

# ============================================================
# Using Instance Methods
# ============================================================

# Object creation is required for instance methods
student1 = Student()
student1.set_details("Arjun", 9)
student1.get_details()

# Static methods can be called using an object,
# but this is NOT recommended and adds confusion
print(student1.greet_user())
