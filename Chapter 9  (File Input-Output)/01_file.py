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
f = open("introduction.txt")
data = f.read()
print(data)
f.close()

