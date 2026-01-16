#               Multiple Context Managers using with (Python 3.10+)
# MULTIPLE CONTEXT MANAGERS

# ------------------------
# Parentheses let us manage multiple resources
# without line breaks or backslashes.

print("\n---------------- MULTIPLE CONTEXT MANAGERS ----------------")

with (
    open("file1.txt") as f1,
    open("file2.txt") as f2
):
    data1 = f1.read()
    data2 = f2.read()

    print("File 1 length:", len(data1))
    print("File 2 length:", len(data2))
# ------------------------