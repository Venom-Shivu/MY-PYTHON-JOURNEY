                                # Repeat Program 4 for a list of such words to be censorerd..

"""
This program reads a file and replaces multiple
censored words with '#####' in the same file.
"""

# List of words that need to be censored
censored_words = ["Error", "fail", "bug", "crash"]

# Open the file in read mode with proper encoding
with open("debug_life.txt", "r", encoding="utf-8") as file:
# encoding="utf-8" is used to correctly read and write files that may contain
# special characters, symbols, or text copied from different sources.
# This prevents UnicodeDecodeError, especially on Windows systems.

    content = file.read()

# Replace each censored word with #####
for word in censored_words:
    content = content.replace(word, "#####")

# Write the updated content back to the same file
with open("debug_life.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("All censored words have been replaced successfully.")

