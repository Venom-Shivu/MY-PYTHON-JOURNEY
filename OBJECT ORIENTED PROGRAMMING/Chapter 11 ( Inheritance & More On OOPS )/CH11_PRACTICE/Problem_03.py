# Create a class 'Employee' and add salary and increment properties to it.
"""Write a method 'salaryAfterIncrement' method with a @property decorator witha setter which
changes the value of increment based on salary. """


# EMPLOYEE CLASS WITH SALARY INCREMENT (PERCENTAGE BASED)

class Employee:
    # Class attribute (shared by all employees)
    company = "Venom Corporation Ltd."

    def __init__(self, name, salary, increment_percent):
        # Instance attributes (unique to each employee)
        self.name = name
        self.salary = salary
        self.increment_percent = increment_percent

    def apply_increment(self):
        #Increases salary based on increment percentage.
        self.salary = self.salary + self.salary * (self.increment_percent / 100)
 # Now the salary will get incremented by the percentage of increment provided by us.
    def details(self):
       
        print(f"Name      : {self.name}")
        print(f"Salary   : ₹{int(self.salary)}")
        print(f"Increment: {self.increment_percent}%")
        print(f"Company  : {self.company}")
        print("-" * 30)


e1 = Employee("Shivansh", 100_000, 10) # The Salary will be ₹1,10,000 as 10% increment
e1.company = "Google"   # Instance attribute overrides class attribute
e1.apply_increment()
e1.details()

e2 = Employee("Rohit", 80_000, 12)
e2.apply_increment()
e2.details()

e3 = Employee("Aman", 60_000, 15)
e3.company = "Microsoft"
e3.apply_increment()
e3.details()




