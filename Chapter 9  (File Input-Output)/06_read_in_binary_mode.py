f = open("Myfile.txt", "rb")
# Opens the file in binary read mode
# Data is read as bytes, not text

data = f.read()
print(data)

f.close()
# Closes the file
