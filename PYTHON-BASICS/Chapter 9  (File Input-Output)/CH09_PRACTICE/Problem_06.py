            # Write a program to mine a log file and find out whether it contains 'python'.

"""
This program reads a log file and checks
whether the word 'python' is present in it.
"""

# Open the log file in read mode using UTF-8 encoding
# UTF-8 avoids errors if the file contains special characters
with open("log_file.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Convert content to lowercase to make the search case-insensitive
if "python" in content.lower():
    print("The log file contains the word 'Python'.")
else:
    print("The log file does NOT contain the word 'Python'.")


