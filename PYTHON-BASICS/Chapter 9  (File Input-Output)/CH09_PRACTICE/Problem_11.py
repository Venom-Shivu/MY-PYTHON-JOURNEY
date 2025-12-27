#  Write a python program to rename a file to "renamed_by_python.txt"
"""
This program renames an existing file
to 'renamed_by_python.txt'.
"""

import os  # Provides functions to interact with the operating system

# Original file name
old_name = "sample_file.txt"

# New file name
new_name = "renamed_by_python.txt"

# Rename the file
os.rename(old_name, new_name)

print(f"File '{old_name}' renamed to '{new_name}' successfully.")

'''     Another Way
import shutil
shutil.move("old_name.txt", "new_name.txt")
This will also do the same thing more easily than os module 

'''



