"""
===========================================
            JOIN METHOD IN PYTHON
===========================================

The join() method combines multiple strings into
a single string using a specified separator.

Syntax:
    separator.join(iterable)

Important:
- The iterable must contain ONLY strings
- Non-string elements will raise an error
"""

# -------------------------------------------
# Example 1: Basic join with space
# -------------------------------------------

words = ["Python", "is", "powerful"]

print("NORMAL JOIN USING SPACE")
print("Result:", " ".join(words))
print()


# -------------------------------------------
# Example 2: Join with different separators
# -------------------------------------------

print("JOIN USING HYPHEN")
print("Result:", "-".join(words))
print()

print("JOIN USING COMMA")
print("Result:", ", ".join(words))
print()


# -------------------------------------------
# Example 3: Joining characters of a string
# -------------------------------------------

text = "PYTHON"

print("JOINING CHARACTERS OF STRING")
print("Result:", " ".join(text))
print()


# -------------------------------------------
# Example 4: Handling non-string elements
# -------------------------------------------

data = ["Python", "Version", 3]

print("JOIN WITH NON-STRING ELEMENT")
print("Fix: Convert all elements to string")

result = " ".join(map(str, data))
print("Result:", result)
print()


# -------------------------------------------
# Summary
# -------------------------------------------

print("SUMMARY")
print("join() is used to efficiently combine strings")
print("Separator defines how elements are connected")
print("All elements must be strings")
print("Use map(str, iterable) to convert non-strings")
