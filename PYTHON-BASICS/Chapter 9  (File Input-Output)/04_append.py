st = "Hey, my name is Shivansh Yadav.\n" \
     "I specialize in data analysis with a strong foundation in Linux-based environments.\n" \
     "I am comfortable working with the Linux command line, file systems, and process management.\n" \
     "My skill set includes data cleaning, analysis, and automation using Python.\n" \
     "I focus on writing efficient, structured code for real-world data-driven problems.\n"

f = open("Myfile.txt", "a")
# Opens the file in append mode.
# Creates the file if it does not exist and adds content at the end if it does.

f.write(st)
# Appends the content to the file

f.close()
# Properly closes the file and releases system resources
