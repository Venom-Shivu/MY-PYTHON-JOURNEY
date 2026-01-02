# Write a program to greet all the person names stored in a list "l" and which starts with "S".

L = ["Shivansh", "Siddharth", "Rohan", "Rahul", "Sakshi", "Riya", "Sanvi", "Satyam", "Akshay","Shobhit", "Shubhankar", "Anupam", "Swapnil", "Sudhanshu"]

for name in L:
    if(name.startswith("S")):
        print(f"Hello {name}! Welcome to the World of Python Programming.\n")
# The {for name in L:} loop iterates through each name in the list L, which contains various person names,
# The if condition {if(name.startswith("S")):} checks if the current name starts with the letter "S".
# If the condition is true, it prints a greeting message for that name using an f-string for formatting.