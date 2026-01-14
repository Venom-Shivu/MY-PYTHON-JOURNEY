"""
Problem Statement:
Write a Python program that attempts to open and read the contents of multiple text files 
(1.txt, 2.txt, 3.txt). If any file is missing, the program should display a clear warning 
message for that file without terminating execution, ensuring that remaining files are 
still processed.
"""

# List of files to be processed
file_names = ["1.txt", "2.txt", "3.txt"]

for file_name in file_names:
    try:
        # Attempt to open and read the file
        with open(file_name, "r") as file:
            print(f"\n--- Contents of {file_name} ---")
            print(file.read())

    except FileNotFoundError:
        # Handles missing file without stopping the program
        print(f"\nWarning: '{file_name}' not found. Skipping this file.")

    except PermissionError:
        # Handles access-related issues explicitly
        print(f"\nError: Permission denied while accessing '{file_name}'.")

    except Exception as error:
        # Fallback for unexpected errors (logged, not hidden)
        print(f"\nUnexpected error while processing '{file_name}': {error}")
