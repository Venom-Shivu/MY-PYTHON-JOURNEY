"""
Create an empty dictionary. Allow 4 friends to enter their favourite languages
as value and use key as their names. Assume that their names are unique.
"""
d = {}
for i in range(4):
    name = input(f"Enter friends name {i+1} :")
    language = input(f"Enter Language name {i+1} :")
    d.update({name:language}) # Full dictionary will all the key value pairs print

 #d.update({name:language}) If we put this here then only last dictionary will be printed

print(d)