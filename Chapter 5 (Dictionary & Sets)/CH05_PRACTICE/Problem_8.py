# If language of two friend are same ; what will happen to program in problem 6
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

# Nothing will happen
"""
name : key and language : value
Different Keys(name) may contain same values(language)  for different pairs 
but the key(name) will be unique and can't be  used more than once. 
You have to use another key(name) "KEY IS THE IDENTIFIER IN DICTIONARY" 
"""