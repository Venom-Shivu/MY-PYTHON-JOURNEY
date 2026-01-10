from typing import List, Tuple, Dict, Optional, Union


# -------------------------------------------------
# 1. List Type Hint
# -------------------------------------------------
print("\n---------------- LIST TYPE HINT ----------------")

def process_items(items: List[str]) -> None:
    # expects a list of strings
    for item in items:
        print(item)

process_items(["apple", "banana", "cherry"])


# -------------------------------------------------
# 2. Tuple Type Hint
# -------------------------------------------------
print("\n---------------- TUPLE TYPE HINT ----------------")

def get_coordinates() -> Tuple[int, int]:
    # always returns (x, y)
    return 10, 20

coords = get_coordinates()
print(coords)


# -------------------------------------------------
# 3. Dict Type Hint
# -------------------------------------------------
print("\n---------------- DICT TYPE HINT ----------------")

def get_student_scores() -> Dict[str, int]:
    # student name -> score
    return {
        "Alice": 90,
        "Bob": 85
    }

scores = get_student_scores()
print(scores)


# -------------------------------------------------
# 4. Optional Type Hint
# -------------------------------------------------
print("\n---------------- OPTIONAL TYPE HINT ----------------")

def greet_user(name: Optional[str] = None) -> str:
    # name can be a string or None
    if name is None:
        return "Hello, Guest!"
    return f"Hello, {name}!"

print(greet_user())
print(greet_user("Alice"))


# -------------------------------------------------
# 5. Union Type Hint
# -------------------------------------------------
print("\n---------------- UNION TYPE HINT ----------------")

def process_value(value: Union[int, str]) -> None:
    # value can be int or str
    if isinstance(value, int):
        print(f"Integer detected → squared: {value ** 2}")
    else:
        print(f"String detected → length: {len(value)}")

process_value(42)
process_value("Hello")


# -------------------------------------------------
# 6. Realistic Example (Optional + Dict)
# -------------------------------------------------
print("\n---------------- REALISTIC EXAMPLE ----------------")

def find_user(user_id: int) -> Optional[Dict[str, str]]:
    # returns None if user doesn't exist
    users = {
        1: {"name": "Alice"},
        2: {"name": "Bob"}
    }
    return users.get(user_id)

print(find_user(1))
print(find_user(99))
# -------------------------------------------------