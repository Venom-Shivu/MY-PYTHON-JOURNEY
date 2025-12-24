# ------------------------------------------------------------
# USING 'with' STATEMENT FOR FILE HANDLING IN PYTHON
# ------------------------------------------------------------

# Writing data to a file using 'with'
st = "Linux-based Data Analyst with strong Python skills.\n" \
     "Focused on data analysis, automation, and clean coding practices.\n"

with open("Myfile.txt", "a") as f:
    # Opens the file in append mode
    # Automatically closes the file after this block
    f.write(st)
    # Writes content safely to the file


# Reading the file content using 'with'
with open("Myfile.txt", "r") as f:
    # Opens the file in read mode
    content = f.read()
    # Reads the entire file content
    print(content)
    # Displays the file content
# We dont't have to explicitly close the file. The file gets auto closed when we came out of with statement.