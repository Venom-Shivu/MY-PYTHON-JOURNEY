#               DICTIONARY MERGE & UPDATE OPERATORS

# -------------------------------------------------
''' 1. Introduced in Python 3.9, the dictionary merge (|) and update (|=)
    2. operators provide a concise way to combine and modify dictionaries.'''
# -------------------------------------------------

# |   → creates a new dictionary
# |=  → updates an existing dictionary in place
# If keys clash, the right-hand dictionary wins.

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

print("\n---------------- DICT MERGE (|) ----------------")

# merge without touching the originals
merged = dict1 | dict2

print("dict1 :", dict1)
print("dict2 :", dict2)
print("merged:", merged)


print("\n---------------- DICT UPDATE (|=) ----------------")

# update dict1 directly (mutation is intentional here)
dict1 |= dict2

print("dict1 after |= :", dict1)


print("\n---------------- REALISTIC EXAMPLE ----------------")

# common use case: defaults + overrides
default_config = {
    "theme": "light",
    "debug": False,
    "timeout": 30
}

user_config = {
    "debug": True,
    "timeout": 60
}

final_config = default_config | user_config
print("final_config:", final_config)
