#   Write a program to wipe out the content of a file using python

"""""
This program demonstrates two ways to wipe out
the content of a file in Python.
"""

# Method 1: Using 'pass'
# Opening a file in write mode ('w') already clears its content.
# 'pass' is used because no writing operation is required.
with open("this_copy.txt", "w", encoding="utf-8"):
    pass


# Method 2: Using f.write("")
# This also wipes the file, but by explicitly writing an empty string.
# The file is still cleared mainly because of 'w' mode, not because of write().
with open("this_copy.txt", "w", encoding="utf-8") as f:
    f.write("")


print("File content has been wiped Successfully.")
