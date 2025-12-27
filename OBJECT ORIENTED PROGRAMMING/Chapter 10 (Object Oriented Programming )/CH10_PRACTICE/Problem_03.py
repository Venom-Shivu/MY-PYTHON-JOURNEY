''' Create a class with a class attribute a; create an object from it and set 'a' directly using object.a= 0. 
      Does this change the class attribute?'''


# Create a class with a class attribute
class Demo:
    a = 10      # Class attribute (shared by all objects)

# Create an object of the class
object = Demo()

# Access class attribute using object
print(object.a)   # Output: 10 (comes from the class) because instance attribute is not present

# Set 'a' using the object
object.a = 0     # This creates an INSTANCE attribute, not class attribute

# Check values
print(object.a)   # Output: 0 (instance attribute)
print(Demo.a)  # Output: 10 (class attribute remains unchanged)

# PROOF:  Checking the contents of Object and Demo
print(object.__dict__)    # {'a': 0}
print(Demo.__dict__['a'])  # 10

''' No. Setting object.a = value does NOT change the class attribute. 
It creates a new instance attribute that hides the class attribute for that object only.'''