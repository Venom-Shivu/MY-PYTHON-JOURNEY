#   Create a class "Programmer" for storing information of few programmers working at Microsoft.


# Class to store information about programmers working at Microsoft
class Programmer:

    # Class variable (same for all programmers)
    company = "Microsoft"

    # Constructor: runs automatically when an object is created
    def __init__(self, name, salary, city, pincode):
        # Store data inside the object
        self.name = name
        self.salary = salary
        self.city = city
        self.pincode = pincode

    # Method to display programmer details
    def show_details(self):
        
        print("-" * 60)
        print(f"The Details of Programmer {self.name} :")
        print(f"Name     : {self.name}")
        print(f"Company  : {self.company}")
        print(f"Salary   : {self.salary}")
        print(f"City     : {self.city}")
        print(f"Pincode  : {self.pincode}")
        print("-" * 60)


# Creating objects of the Programmer class
shiva = Programmer("Venom", 1_000_000, "Lucknow", 226301)
shiva.show_details()

rahul = Programmer("Rahul", 1_200_000, "Bangalore", 560001)
rahul.show_details()

sakshi = Programmer("Sakshi", 1_500_000, "Punjab", 140001)
sakshi.show_details()

venom = Programmer("Shivansh", 2_000_000, "Lucknow", 226001)
venom.show_details()

aarav = Programmer("Aarav", 100_000, "Delhi", 110001)
aarav.show_details()






