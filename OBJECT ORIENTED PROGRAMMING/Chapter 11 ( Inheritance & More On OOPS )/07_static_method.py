# ============================================================
#                       STATIC METHODS
# ============================================================
"""
WHAT IS A STATIC METHOD?
------------------------
A static method is a method that belongs to a class but does NOT
depend on:
- the object (self)
- the class itself (cls)

It is placed inside a class only because it is logically related
to that class.

WHEN TO USE:
- Utility functions
- Helper calculations
- Validation logic
"""

class MathOperations:
    """
    This class groups mathematical utility functions.
    No object data is required to use these methods.
    """

    @staticmethod
    def add(a, b):
        # Performs addition using only the given inputs
        # No access to instance or class data
        return a + b

    @staticmethod
    def subtract(a, b):
        # Performs subtraction
        return a - b

    @staticmethod
    def greet():
        # Simple utility method with no dependency on object or class
        print("Hello! I am a static method inside MathOperations.")


# ============================================================
#                   USAGE & DEMONSTRATION
# ============================================================

# Preferred way: call static methods using the CLASS name
print("Using class name:")
print(f"Addition    : {MathOperations.add(10, 5)}")
print(f"Subtraction : {MathOperations.subtract(10, 5)}")
MathOperations.greet()

# Static methods CAN be called using an object,
# but this is discouraged because it suggests instance usage
print("\nUsing object (works but not recommended):")
obj = MathOperations()
print(f"Addition    : {obj.add(20, 20)}")


# ============================================================
#                       FINAL NOTE
# ============================================================
"""
Static methods:
- Do NOT receive self
- Do NOT receive cls
- Do NOT modify object or class state

If a method needs:
- object data → use INSTANCE METHOD
- class data  → use CLASS METHOD
- neither     → use STATIC METHOD
"""
