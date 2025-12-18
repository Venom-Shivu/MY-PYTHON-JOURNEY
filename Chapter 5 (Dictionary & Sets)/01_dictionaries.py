marks = {

    "Shivansh":85,
    "Aryan":90,
    "Anjali":78,
    "Rohit":92,
    "Sneha":88
    
} #List of Key Value Pairs

print(marks,type(marks))
#print(marls[90])  This will show a error
print(marks["Shivansh"]) # This will return the string corresponding to "Shivansh" i.e 85,(dictionary)
#This is very useful for lookup in large datasets in O(1) time (time complexity)
# Dictionaries are unordered, indexed, cannot contain duplicate keys and mutable , we can edit, remove or add values.



