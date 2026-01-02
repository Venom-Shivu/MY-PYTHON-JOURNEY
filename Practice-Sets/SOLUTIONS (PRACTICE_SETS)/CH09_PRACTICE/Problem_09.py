#  Write a program to find out wheteher a file is identical & matches the content of another file.
"""
This program checks whether two files have
exactly the same content.
"""

# Open the first file and read its content
with open("this.txt", "r", encoding="utf-8") as file1:
    content1 = file1.read()

# Open the second file and read its content
with open("this_copy.txt", "r", encoding="utf-8") as file2:
    content2 = file2.read()

# Compare the contents of both files
if content1 == content2:
    print("Both files are identical.")
else:
    print("The files are NOT identical.")
