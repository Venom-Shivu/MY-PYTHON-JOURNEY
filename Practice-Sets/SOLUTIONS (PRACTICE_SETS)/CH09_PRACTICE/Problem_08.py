        # Write a Program to make a copy of a text file "this.txt"
"""
This program creates a copy of the file 'this.txt'
by reading its content and writing it to another file.
"""

# Open the source file in read mode
with open("this.txt", "r", encoding="utf-8") as source:
    content = source.read()   # Read entire file content

# Open the destination file in write mode
with open("this_copy.txt", "w", encoding="utf-8") as destination:
    destination.write(content)   # Write content to the new file

print("File copied successfully.")


