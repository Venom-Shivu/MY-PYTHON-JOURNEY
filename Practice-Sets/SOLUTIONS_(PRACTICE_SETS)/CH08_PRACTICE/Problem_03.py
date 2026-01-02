#   How do you prevent a python print() funtion to print a new line at the end.

# Use 'end' to override the default newline (\n) with a custom character.

print("a", end = " ")  # Ends with a space instead of a newline
print("b", end = ":")  # Ends with a colon
print("c", end = ",")  # Ends with a comma
print("d", end = "")   # Ends with nothing (joins 'd' and 'e' directly)
print("e")             # Default behavior: ends with a newline but the cursor is previously at d so it prints "de"

# EXPLANATION:
# By default, print() has end="\n" (newline). 
# By manually defining 'end', we tell Python what to put at the very end of the string.
# This allows us to keep multiple print statements on the same line.

#end: What happens at the very end of the print call.

#sep: What happens between multiple items inside one print call.

print("Apples", "Bananas", "Cherries", sep=", ", end=".") # If we do not use sep then it does not print commas in between
# Output: Apples, Bananas, Cherries.