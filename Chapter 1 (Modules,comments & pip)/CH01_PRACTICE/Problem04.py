import os

def print_directory_contents(path):
    try:
        entries = os.listdir(path)       # get list of entries in the directory
    except FileNotFoundError:
        print(f"Error: directory '{path}' does not exist.")
        return
    except PermissionError:
        print(f"Error: permission denied for directory '{path}'.")
        return

    print(f"Contents of directory '{path}':")
    for entry in entries:
        print(entry)

if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    print_directory_contents(dir_path)
    
# The above code the os module to print the contents of a directory (both files and sub-folders)
# Explanation

# The function os.listdir(path) returns a list of names (files + directories) in the directory specified by path. 
# We catch FileNotFoundError and PermissionError to handle common error cases.
# The program prints each entry in the directory.
