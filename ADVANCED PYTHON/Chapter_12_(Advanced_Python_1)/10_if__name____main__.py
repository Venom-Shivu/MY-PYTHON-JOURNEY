"""
==================================================
Understanding __name__ and __main__ in Python
==================================================

Goal:
-----
Explain how Python determines whether a file is:
1) Executed directly
2) Imported as a module

This pattern controls execution flow and prevents
unintended side effects during imports.
"""

# --------------------------------------------------
# SECTION 1: __name__ (Module Identity)
# --------------------------------------------------
"""
__name__:
- Automatically assigned by Python
- Identifies the current module
- Changes based on how the file is used
"""

print("Current module name:", __name__)


def display_module_identity():
    """
    Prints the name of the module this function belongs to.
    Useful for understanding execution context.
    """
    print("Function executed inside module:", __name__)


# --------------------------------------------------
# SECTION 2: "__main__" (Entry Point Marker)
# --------------------------------------------------
"""
"__main__":
- A special string used by Python
- Assigned only to the starting file
- Helps isolate execution-only logic
"""

if __name__ == "__main__":
    print("\nThis file is the program entry point")
else:
    print("\nThis file is being imported")


# --------------------------------------------------
# SECTION 3: Reusable Logic (Safe for Import)
# --------------------------------------------------

def multiply(a, b):
    """
    Performs multiplication.

    Designed to be reusable without triggering
    automatic execution.
    """
    return a * b


# --------------------------------------------------
# SECTION 4: Controlled Execution (Combined Example)
# --------------------------------------------------

if __name__ == "__main__":
    """
    This block runs only when:
        python name_main_professional.py

    It will NOT execute when imported elsewhere.
    """

    print("\n--- Executing main logic ---")

    display_module_identity()

    result = multiply(6, 7)
    print("Multiplication result:", result)

    print("--- Execution complete ---")
