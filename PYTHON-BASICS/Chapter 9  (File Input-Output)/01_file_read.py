'''                        ------------------------------------------------------------
                                       FILE I/O - PRACTICAL CONTEXT
                           ------------------------------------------------------------
 Suppose we have a very long string that contains email addresses.
 During program execution, these emails are extracted temporarily
 (for example, using regex or string processing).'''

# Example:
#   a = "a very long string with emails"
#   emails = ["shiva@gmail.com", "shiva@yahoo.com"]
#
# The extraction process may take time (e.g., a few seconds),
# but once the program terminates, the extracted emails are lost
# because they exist only in memory (RAM).
#
# This is where File I/O becomes important.
# By writing the extracted emails to a file, we can store them
# permanently on disk for later use.
#
# FILE I/O stands for File Input/Output.
# It allows a program to:
#   - Write data to files (Output)
#   - Read data from files (Input)
#
# File I/O is essential for persistence, meaning data remains
# available even after the program stops running.
# This makes it a core concept for real-world applications.
# ------------------------------------------------------------

#                       ====================================================================
#                                                  READING A FILE
#                       ====================================================================


"""
f = open("introduction.txt") Opens the file in read mode
data = f.read() Reads the entire content of the file and stores it in the 'data' variable
print(data) Prints the content of the file
f.close() Closes the file
"""

# This works ONLY when the current working directory is the same
# folder where 'introduction.txt' exists.
#
# If the program is run from the main project folder
# (MY_PYTHON_JOURNEY), Python searches for the file there
# and raises FileNotFoundError because the file is inside Chapter 9.
# This is a working-directory issue, not a file or Python issue.


from pathlib import Path
# Used to work with file paths easily and safely

BASE_DIR = Path(__file__).parent
# Gets the folder where this Python file is located

file_path = BASE_DIR / "introduction.txt"
# Creates the full path to introduction.txt in the same folder

with open(file_path, "r") as file:
    # Opens the file in read mode and auto-closes it
    print(file.read())
    # Reads and prints the entire file content

