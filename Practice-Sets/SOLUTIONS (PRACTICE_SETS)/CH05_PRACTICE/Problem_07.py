        # If the names of the two friends are same ; what happens to program in problem 6
"""
Create an empty dictionary. Allow 4 friends to enter their favourite languages
as value and use key as their names. Assume that their names are unique.
"""
d = {}
for i in range(4):
    name = input(f"Enter friends name {i+1} :")
    language = input(f"Enter Language name {i+1} :")
    d.update({name:language}) 
# Update function adds,updates key value pairs
 #d.update({name:language}) If we put this here then only last dictionary will be printed

print(d)

""" If we enter the name twice then, it will return the last  entered input(key-value pair) 
because we are using update so it will update the previous Key value pair with new.
"""