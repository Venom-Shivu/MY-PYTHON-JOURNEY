""" A file contains a word "Error" multiple times. You need to write a program which replace this word with ##### by updating the same file"""


"""
This program reads a file and replaces every occurrence
of the word 'Error' with '#####' in the same file.
"""
# Read the file using UTF-8 encoding
with open("debug_life.txt", "r", encoding="utf-8") as file:
# encoding="utf-8" is used to correctly read and write files that may contain
# special characters, symbols, or text copied from different sources.
# This prevents UnicodeDecodeError, especially on Windows systems.

    content = file.read()

# Replace all occurrences of 'Error' with '#####'
updated_content = content.replace("Error", "#####")

# Write the updated content back to the same file
with open("degub_life.txt", "w", encoding="utf-8") as file:
    file.write(updated_content)

print("All occurrences of 'Error' have been replaced with '#####'.")


