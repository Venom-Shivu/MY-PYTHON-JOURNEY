# ============================================================
#                        super() METHOD
# ============================================================
"""
WHAT IS super()?
----------------
super() is a built-in function used in inheritance.

It allows a child class to call methods (usually __init__)
from its parent class.

WHY super() IS IMPORTANT:
- It ensures parent class attributes are initialized
- It maintains the correct order of execution
- It avoids code duplication
- It is mandatory in multi-level inheritance
"""

# ============================================================
#                   SIMPLE & CLEAN EXAMPLE
# ============================================================

class Grandparent:
    def __init__(self):
        # Attribute defined at the grandparent level
        self.grandparent_name = "Abhay"
        print(">> Grandparent constructor executed")


class Parent(Grandparent):
    def __init__(self):
        # Calls Grandparent's __init__()
        # Without this, grandparent_name would NOT exist
        super().__init__()

        # Attribute defined at the parent level
        self.parent_name = "Rahul"
        print(">> Parent constructor executed")


class Child(Parent):
    def __init__(self):
        # Calls Parent's __init__()
        # Parent then calls Grandparent automatically
        super().__init__()

        # Attribute defined at the child level
        self.child_name = "Rohit"
        print(">> Child constructor executed")


# ============================================================
#                   OBJECT CREATION & OUTPUT
# ============================================================

print("\n================= OBJECT CREATION =================\n")

print("--- Creating Grandparent Object ---")
g = Grandparent()

print("\n--- Creating Parent Object ---")
p = Parent()

print("\n--- Creating Child Object ---")
c = Child()

# ============================================================
#               ACCESSING INHERITED ATTRIBUTES
# ============================================================

print("\n================= FINAL CHECK =================\n")

# Because of super(), the child object has access
# to attributes from ALL parent classes
print(
    f"{c.child_name} is the child of {c.parent_name} "
    f"and the grandchild of {c.grandparent_name}"
)

print("\n=================================================")
