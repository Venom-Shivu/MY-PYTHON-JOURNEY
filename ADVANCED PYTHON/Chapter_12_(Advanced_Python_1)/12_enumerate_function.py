"""
=====================================================
            ENUMERATE FUNCTION IN PYTHON
=====================================================

What enumerate() does:
- Attaches an index to each element of an iterable
- Eliminates manual counter variables
- Produces clean, readable, and bug-free loops

Why it exists:
- Manual indexing is verbose and error-prone
- enumerate() solves that problem directly

Syntax:
    enumerate(iterable, start=0)
"""

# ---------------------------------------------------
# Sample iterable used in all examples
# ---------------------------------------------------
data = ["Venom", 5, 56, 44.5, 34.5, "Shivansh", "Shiva"]

print("\n========== EXAMPLE 1 : BASIC ENUMERATE ==========")

# Default behavior: index starts from 0
for index, value in enumerate(data):
    print(f"Index {index} -> {value}")


print("\n========== EXAMPLE 2 : ENUMERATE WITH START VALUE ==========")

# Start index from 1 (useful for human-readable output)
for index, value in enumerate(data, start=1):
    print(f"Item number {index} is {value}")


print("\n========== EXAMPLE 3 : FILTERING WITH ENUMERATE ==========")

# Use enumerate when index matters in logic
for index, value in enumerate(data):
    if isinstance(value, (int, float)):
        print(f"Numeric value found at index {index}: {value}")


print("\n========== EXAMPLE 4 : ENUMERATE WITH CONDITIONS ON INDEX ==========")

# Operate based on index position
for index, value in enumerate(data):
    if index % 2 == 0:
        print(f"Even index {index} contains -> {value}")


print("\n========== EXAMPLE 5 : ENUMERATE ON STRING ==========")

# enumerate works on strings character by character
name = "PYTHON"

for index, char in enumerate(name):
    print(f"Character at position {index} is '{char}'")


print("\n========== EXAMPLE 6 : ENUMERATE WITH LIST CONVERSION ==========")

# enumerate returns an enumerate object
enum_object = enumerate(data)

# Converting enumerate object to list
enum_list = list(enum_object)

print("Enumerate converted to list:")
print(enum_list)


print("\n========== EXAMPLE 7 : ENUMERATE WITH BREAK ==========")

# Stop loop when a condition is met
for index, value in enumerate(data):
    if value == "Shivansh":
        print(f"Found '{value}' at index {index}")
        break


print("\n========== EXAMPLE 8 : COMPARISON (BAD vs GOOD) ==========")

#  BAD PRACTICE: Manual counter
counter = 0
for value in data:
    print(f"Manual Counter -> {counter} : {value}")
    counter += 1

print("\n--- Using enumerate (CORRECT WAY) ---")

#  GOOD PRACTICE: enumerate
for index, value in enumerate(data):
    print(f"Enumerate -> {index} : {value}")


print("\n========== EXAMPLE 9 : ENUMERATE IN REALISTIC SCENARIO ==========")

# Simulating menu options
menu = ["Add User", "Delete User", "Update User", "Exit"]

for option_number, option in enumerate(menu, start=1):
    print(f"{option_number}. {option}")


print("\n========== END OF ENUMERATE DEMONSTRATION ==========")
