f = open("Myfile.txt", "r")
# Opens the file in text read mode (default mode)

data = f.read()
print(data)

f.close()
# Closes the file
