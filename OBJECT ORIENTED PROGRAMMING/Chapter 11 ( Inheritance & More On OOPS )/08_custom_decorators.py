# ============================================================
#                       CUSTOM DECORATORS
# ============================================================
"""
WHAT IS A DECORATOR?
--------------------
A decorator is a function that:
1. Takes another function as input
2. Adds extra behavior to it
3. Returns a new function (wrapped version)

Important:
- The original function is NOT modified
- The behavior is extended by wrapping it

Syntax:
@decorator_name
def function():
    pass
"""

from functools import wraps   # Used to preserve function metadata


# ============================================================
#                   DECORATOR DEFINITION
# ============================================================

def greet_decorator(func):
    """
    This decorator adds messages before and after
    the execution of the target function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Code that runs BEFORE the original function
        print("\n>> [Decorator] Before function execution")

        # Call the original function with its arguments
        result = func(*args, **kwargs)

        # Code that runs AFTER the original function
        print(">> [Decorator] After function execution")

        # Return the original function's result (if any)
        return result

    # Return the wrapped function
    return wrapper


# ============================================================
#                   APPLYING THE DECORATOR
# ============================================================

@greet_decorator
def hello():
    """Prints a greeting message"""
    print("   Hello World! I am the main function.")


@greet_decorator
def bye():
    """Prints a farewell message"""
    print("   Goodbye! See you soon.")


# ============================================================
#                   USAGE & OUTPUT
# ============================================================

# Calling hello() actually calls wrapper()
hello()

bye()


# ============================================================
#                   FINAL EXPLANATION
# ============================================================
"""
@decorator syntax is just shorthand.

This:
@ greet_decorator
def hello():
    pass

Means this:
hello = greet_decorator(hello)

Decorator execution order:
1. Decorator wraps the function (once)
2. Wrapper runs every time the function is called
"""
