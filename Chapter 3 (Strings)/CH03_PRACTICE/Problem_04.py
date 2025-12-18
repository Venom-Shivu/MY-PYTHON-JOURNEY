# REPLCE THE DOUBLE SPACE FROM THE PROBLEM 3 WITH SINGLE SPACE


name = " Shivansh is good at  Python  Programming"
# Replacing double spaces with single space using the replace() method.

print(name.replace ("  ", " "))
# Output:  Shivansh is good at Python Programming  
# This function prints a new string where all double spaces are replaced with single spaces, 
# without modifying the original string name(). This is acalled immutable property of strings in Python.

#Another way to replace double spacces with sinle space using variable.
corrected_name = name.replace("  ", " ")
print("Corrected String:", corrected_name)
# Output: Corrected String:  Shivansh is good at Python Programming