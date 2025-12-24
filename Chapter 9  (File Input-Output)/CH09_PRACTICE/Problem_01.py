''' Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'.'''

# Program to check whether the word 'twinkle' exists in poems.txt

# Open the file in read mode
with open("poems.txt", "r") as file:
    content = file.read()   # Read entire file content as a string

# Convert text to lowercase to make the search case-insensitive
if "twinkle" in content.lower():
    print("The word 'twinkle' is present in the file.")
else:
    print("The word 'twinkle' is NOT present in the file.")
