st = "Updating profile:\n" \
     "Linux-based Data Analyst with hands-on experience in Python automation.\n" \
     "Focused on data processing, analysis, and system-level efficiency.\n\n"

f = open("Myfile.txt", "r+")
# Opens the file in read + write mode
# Allows reading existing content and writing new content

print(f.read())
# Reads and displays existing file content

f.write(st)
# Writes updated content at the current file pointer position

f.close()
# Closes the file properly
