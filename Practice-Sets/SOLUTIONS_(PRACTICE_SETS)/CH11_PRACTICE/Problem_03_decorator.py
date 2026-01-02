# Create a class 'Employee' and add salary and increment properties to it.
"""Write a method 'salaryAfterIncrement' method with a @property decorator witha setter which
changes the value of increment based on salary. """

# ============================================================
# EMPLOYEE CLASS USING @property AND @setter
# ============================================================

class Employee:
    company = "Venom Corporation Ltd."

    def __init__(self, name, salary, increment_percent):
        # Base salary (before increment)
        self.name = name
        self.salary = salary
        self.increment_percent = increment_percent

    # --------------------------------------------------------
    # PROPERTY: Computed salary after increment
    # --------------------------------------------------------
    @property
    def salaryAfterIncrement(self):
        """
        Returns the salary AFTER applying increment percentage.
        Acts like an attribute, but is calculated dynamically.
        """
        return self.salary + (self.salary * self.increment_percent / 100)

    # --------------------------------------------------------
    # SETTER: Adjust increment based on desired final salary
    # --------------------------------------------------------
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, desired_salary):
        """
        Updates increment_percent so that
        salaryAfterIncrement becomes 'desired_salary'.
        """
        if desired_salary <= self.salary:
            raise ValueError("Final salary must be greater than base salary.")

        # Reverse-calculating the increment percentage
        self.increment_percent = ((desired_salary - self.salary) / self.salary) * 100

    # --------------------------------------------------------
    # DISPLAY DETAILS
    # --------------------------------------------------------
    def details(self):
        print(f"Name      : {self.name}")
        print(f"Base Pay  : ₹{int(self.salary)}")
        print(f"Increment : {round(self.increment_percent, 2)}%")
        print(f"Final Pay : ₹{self.salaryAfterIncrement:,.0f}") # Converts number in 000,000 format
        print(f"Company  : {self.company}")
        print("-" * 35)

e1 = Employee("Shivansh", 100_000, 10)

# Access like an attribute, NOT a method
print(f"Initial Increment Percentage : {e1.increment_percent}%")
print(f"Initial Salary After Increment: ₹{e1.salaryAfterIncrement:,.0f}")# Converts number in 000,000 format


# Change final salary → increment auto-adjusts
e1.salaryAfterIncrement = 130_000

e1.details()


class Employee:
    def __init__(self, name, salary, increment):
        self.name = name
        self.salary = salary
        self.increment = increment  # absolute increment amount

    @property
    def salary_after_increment(self):
        """
        Returns total salary after applying increment.
        """
        return self.salary + self.increment

    @salary_after_increment.setter
    def salary_after_increment(self, new_total_salary):
        """
        Updates increment based on desired total salary.
        """
        if new_total_salary < self.salary:
            raise ValueError("Total salary cannot be less than base salary.")
        self.increment = new_total_salary - self.salary

e = Employee("Venom", 100000, 20000)
print(f"Employee Name: {e.name}")
print(f"Initial Increment: {e.increment}")  # 20000
print(f"Initial Pay: {e.salary_after_increment}")           # 100000


e.salary_after_increment = 150000
print(f"Final Increment: {e.increment}")               # 50000
print(f"Final Pay: {e.salary_after_increment}")  # 150000
