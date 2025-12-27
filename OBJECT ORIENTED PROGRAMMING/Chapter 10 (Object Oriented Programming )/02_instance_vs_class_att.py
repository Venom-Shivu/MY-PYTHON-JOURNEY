# ============================================================
#           CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE
# ============================================================

class Employee:
    language = "Python" # Class Attribute: Shared by all objects of this class
    salary = 120000     # Class Attribute

# Creating an object 'shivu'
shivu = Employee()
shivu.name = "Shiva"    # Instance Attribute: Specific to this object only
shivu.language = "Java" # Instance Attribute: This creates a new property for 'shivu' that hides the class attribute

print(f"Name: {shivu.name}")
print(f"Language: {shivu.language}") # Prints "Java" (Instance attribute takes priority)
print(f"Salary: {shivu.salary}")     # Prints 120000 (Falls back to Class attribute)
#print(f"Salary: {shivu.wages}")     # Returns an error-->" AttributeError: 'Employee' object has no attribute 'wages' "

'''
When looking up for shivu.attribute it checks for the following:
        1 ) Is attributes present in Object?
        2 ) Is attributes present in Classs?
        3 ) If not found in either, it raises an AttributeError.
'''
print("-" * 30)

# Creating another object 'rohan'
rohan = Employee()
rohan.name = "Rohan"
print(f"Name: {rohan.name}")
print(f"Language: {rohan.language}") # Prints "Python" (Uses Class attribute because instance attribute is not set)
print(f"Salary: {rohan.salary}")     # Prints 120000 (Uses Class attribute)


# ============================================================
#           ANOTHER EXAMPLE: SHOPPING CART
# ============================================================

class ShoppingCart:
    store_name = "Amazon"  # Class Attribute
    discount = 10          # Class Attribute (10% default discount)

cart1 = ShoppingCart()
cart2 = ShoppingCart()

cart2.discount = 50        # Instance Attribute (Special discount for this user)

print("-" * 30)
print(f"Cart 1 Store: {cart1.store_name}, Discount: {cart1.discount}%") # Uses class defaults (10%)
print(f"Cart 2 Store: {cart2.store_name}, Discount: {cart2.discount}%") # Uses instance specific discount (50%)
