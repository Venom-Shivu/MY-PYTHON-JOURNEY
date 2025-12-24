'''# ------------------------------------------------------------
# READING LINE BY LINE USING readline()
# ------------------------------------------------------------

f = open("introduction.txt", "r")
# Opens the file in read mode (file must be in the current working directory)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

f.close()
# Closes the file after reading


# ------------------------------------------------------------
# READING ALL LINES USING A FOR LOOP (RECOMMENDED)
# ------------------------------------------------------------

print("\n--- Reading all lines using a for loop ---")

f = open("introduction.txt", "r")
for line in f:
    print(line, end='')  # Prevents extra blank lines
f.close()


# ------------------------------------------------------------
# READING ALL LINES USING readlines()
# ------------------------------------------------------------

print("\n--- Reading all lines using readlines() ---")

f = open("introduction.txt", "r")
all_lines = f.readlines()  # Reads all lines into a list

for line in all_lines:
    print(line, end='')

f.close()
'''
#This code gives FileNotFoundError because Python looks for
# "introduction.txt" in the current working directory, not
# in the folder where this script is saved.


from pathlib import Path

file_path = Path(__file__).parent / "introduction.txt"

# ------------------------------------------------------------
# READING LINE BY LINE USING readline()
# ------------------------------------------------------------

with open(file_path, "r") as file:
    line1 = file.readline()
    print(line1)

    line2 = file.readline()
    print(line2)

    line3 = file.readline()
    print(line3)


# ------------------------------------------------------------
# READING ALL LINES USING A FOR LOOP 
# ------------------------------------------------------------

print("\n--- Reading all lines using a for loop ---")
with open(file_path, "r") as file:
    for line in file:
        print(line, end='')  # Prevents extra blank lines


# ------------------------------------------------------------
# READING ALL LINES USING readlines()
# ------------------------------------------------------------

print("\n--- Reading all lines into a list using .readlines() ---")
with open(file_path, "r") as file:
    all_lines = file.readlines()

for line in all_lines:
    print(line, end='')

# ------------------------------------------------------------
# READING ALL LINES USING A WHILE LOOP 
# ------------------------------------------------------------
print("\n--- Reading all lines using a while loop and readline() ---")
with open(file_path, "r") as file:
    line = file.readline()  # Read the first line before entering the loop
    while (line != ""):
        # Loop continues until an empty string is returned (end of file)
        print(line, end='')
    # Print the current line (end='' avoids extra blank lines)
    # Move to the next line
        line = file.readline()
        # Read the next line for the next iteration

