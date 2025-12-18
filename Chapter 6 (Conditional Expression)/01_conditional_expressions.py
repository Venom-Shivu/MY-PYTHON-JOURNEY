"""
If we want to apply several conditions while executing a code then we use conditional expressions, to met the defined criteria
In python programming we must be able to execute instructions on a condtion(s) being met.
"""
#IF ELSE Statement


a = int(input("Enter your age: "))

if(a>=18):
    print("You are an adult and have right to vote in elections")
    print("No need for conset")
# Indentation is autoapplied in python if we work under in conditional statement, if not used then it will through an error.
else:
    print("You are a teenager and do not have right to vote")

print(" End Of Program")
