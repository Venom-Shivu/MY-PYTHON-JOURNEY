st = "Hey, my name is Shivansh Yadav.\n" \
     "I am highly interested in Python programming and write clean, structured code.\n" \
     "I focus on professionalism, logical thinking, and real-world problem solving.\n" \
     "I am continuously improving my skills in Python, data handling, and software development."

f = open("Myfile.txt", "w")
# Opens the file in write mode (creates the file if it does not exist)

f.write(st)
# Writes the complete string content into the file

f.close()
# Properly closes the file and releases system resources
