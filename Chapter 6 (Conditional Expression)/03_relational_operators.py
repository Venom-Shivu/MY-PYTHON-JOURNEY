                        # Relational Operators/Comparison Operators in Python
#1. "==": Equals.
#2. "!=": Not equals to.
#3. ">=" : Greater than or equal to.
#4. "<=" : Lesser than or equal to.

a = int(input("Enter first number for comaprison: "))
b = int(input("Enter second number for comparison: "))

if(a == b):
    print(f"{a} is Equal to {b}")

elif(a != b):
    print(f"{a} is not Equal to  {b}")
elif(a > b):
    print(f"{a} is Greater than {b}")
else:
    print(f"{a} is Lesser than {b}")