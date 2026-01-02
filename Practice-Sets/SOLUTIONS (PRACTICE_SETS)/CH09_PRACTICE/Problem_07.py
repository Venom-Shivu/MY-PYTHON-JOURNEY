# Write a program to find out the line number where Python is present from Problem 6.

"""
This program reads a log file line by line
and prints the line numbers where the word 'python' is found.
"""

# Open the log file in read mode with UTF-8 encoding
with open("log_file.txt", "r", encoding="utf-8") as file:

    # Read file line by line using enumerate to get line numbers
    for line_number, line in enumerate(file, start=1):

        # Convert line to lowercase for case-insensitive search
        if "python" in line.lower():
            print(f"'Python' found at line number: {line_number}")
