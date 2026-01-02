# Add comments to your code explaining what each line does.

import os

def print_directory_contents(path):
    """
    Prints the names of all files and directories in the given path.
    
    Use Cases:
    -----------
    1. To quickly view all items inside a specific folder.
    2. Useful for debugging file operations (checking what's inside a working directory).
    3. Can be extended for filtering (e.g., only list .txt files or only folders).
    4. Helps in automating directory scans before performing file manipulations.
    """
    try:
        # os.listdir() returns a list of all entries (files + folders) in the given directory.
        entries = os.listdir(path)
    except FileNotFoundError:
        # Triggered when the directory does not exist.
        print(f"Error: The directory '{path}' does not exist.")
        return
    except PermissionError:
        # Triggered when the script doesn’t have permission to access the directory.
        print(f"Error: Permission denied for directory '{path}'.")
        return

    # Print the directory name for clarity.
    print(f"\nContents of directory: '{path}'\n" + "-" * 50)

    # Loop through and print each item in the directory.
    for entry in entries:
        print(entry)

    # Summary line showing total count of entries.
    print("-" * 50)
    print(f"Total items: {len(entries)}")

if __name__ == "__main__":
    # Prompt user to input a directory path.
    dir_path = input("Enter the directory path: ").strip()
    
    # Call the function to print contents.
    print_directory_contents(dir_path)
