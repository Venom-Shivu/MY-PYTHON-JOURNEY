"""
FORMAT METHOD IN PYTHON (str.format)

The format() method inserts values into a string at predefined placeholders {}.
It improves readability and avoids manual string concatenation.
"""

# -------------------------------
# Basic example (positional formatting)
# -------------------------------
greeting = "Hello! {} Welcome to {}.".format("Shivansh", "Python")
print(greeting)

# -------------------------------
# Reusing the same format structure
# -------------------------------
language_message = "Hello! {} Welcome to {}."
print(language_message.format("Venom", "Java"))
print(language_message.format("Alex", "C++"))

# -------------------------------
# Formatting different data types
# -------------------------------
device_info = "My {} is {} years old.".format("Laptop", 5)
print(device_info)

# -------------------------------
# Multiple placeholders (clear meaning)
# -------------------------------
activity = "{} loves to {} on {} platforms for {} hours using {}."
print(activity.format(
    "Venom",
    "code",
    "various",
    "10 to 12",
    "Python"
))

# -------------------------------
# Index-based formatting (controls position)
# -------------------------------
indexed_example = "{0} is learning {1}. {0} practices {1} daily."
print(indexed_example.format("Venom", "Python"))

# -------------------------------
# Named placeholders (BEST for readability)
# -------------------------------
profile = "{name} is {age} years old and works with {technology}."
print(profile.format(
    name="Shivansh",
    age=21,
    technology="Python"
))

# -------------------------------
# Formatting numbers
# -------------------------------
price = "The total cost is ₹{:.2f}".format(1499.5678)
print(price)
