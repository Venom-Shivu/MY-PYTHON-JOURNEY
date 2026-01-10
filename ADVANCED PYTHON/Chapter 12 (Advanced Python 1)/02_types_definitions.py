# TYPE DEFINITIONS (Type Hints)
# -----------------------------------------
# Type hints tell the reader what kind of data
# a variable or function is *expected* to work with.
# Python won't enforce them — they’re just guidance.

# -----------------------------
# Variables with type hints
# -----------------------------

age: int = 25              # expected to store an integer
price: float = 199.99      # decimal value
is_logged_in: bool = True  # true / false flag
username: str = "Venom"    # text value

print(f"Age: {age}")
print(f"Price: {price}")
print(f"Logged in: {is_logged_in}")
print(f"Username: {username}")


# -----------------------------
# Function with type hints
# -----------------------------

def greet(name: str) -> str:
    # takes a string and returns a string
    return f"Hello, {name}!"

print(greet("Venom"))


# -----------------------------
# Function with multiple inputs
# -----------------------------

def multiply(a: int, b: int) -> int:
    # simple math, expects integers
    return a * b

print(multiply(4, 5))


# -----------------------------
# Built-in collections (no imports)
# -----------------------------

scores: list = [80, 85, 90]              # list of numbers
student: dict = {"Math": 88, "Science": 92}  # subject → score
location: tuple = (10, 20)               # fixed coordinates

print(scores)
print(student)
print(location)


# -----------------------------
# Function returning a list
# -----------------------------

def get_scores() -> list:
    # returns a list, nothing fancy
    return [75, 82, 91]

print(get_scores())


# -----------------------------
# Important reality check
# -----------------------------
# Python won't stop bad assignments like this:

age = "twenty five"  # still runs, even though the hint says int

# Type hints help humans and tools, not Python itself.

print(f"Age after bad assignment: {age}")