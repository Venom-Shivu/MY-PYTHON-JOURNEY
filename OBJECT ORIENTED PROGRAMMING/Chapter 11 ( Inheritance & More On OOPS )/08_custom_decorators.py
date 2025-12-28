# ============================================================
#                   CUSTOM DECORATORS
# ============================================================

"""
DECORATOR:
----------
A decorator is a function that wraps another function
to add extra behavior without changing the original code.

Common uses:
- Logging
- Validation
- Timing
- Authorization
"""

from functools import wraps   # Keeps original function name & docstring


# ============================================================
#               DECORATOR DEFINITION
# ============================================================

def log_action(func):
    """
    This decorator logs when a function starts and ends.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        *args   → Collects all POSITIONAL arguments passed
                  to the original function as a tuple.

        **kwargs → Collects all KEYWORD arguments passed
                   to the original function as a dictionary.

        Why needed?
        -----------
        Because the decorator should work with ANY function,
        no matter how many arguments it receives.
        """

        # Code executed BEFORE the original function
        print("\n[LOG] Function started:", func.__name__)

        # Call the original function with the SAME arguments
        # *args   → passes positional arguments back
        # **kwargs → passes keyword arguments back
        result = func(*args, **kwargs)

        # Code executed AFTER the original function
        print("[LOG] Function finished:", func.__name__)

        # Return the original function's result (if any) like here is show details()
        return result

    # Return the wrapped version of the function
    return wrapper


# ============================================================
#                   EMPLOYEE CLASS
# ============================================================

class Employee:

    def __init__(self, first_name, last_name):
        # Instance attributes
        self.first_name = first_name
        self.last_name = last_name

    # --------------------------------------------------------
    # DECORATED INSTANCE METHOD
    # --------------------------------------------------------
    @log_action
    def show_details(self):
        """
        This method takes ONLY 'self'.
        'self' will be captured inside *args automatically.
        """
        print(f"Employee Name: {self.first_name} {self.last_name}")

    # --------------------------------------------------------
    # DECORATED METHOD WITH PARAMETERS
    # --------------------------------------------------------
    @log_action
    def update_name(self, full_name):
        """
        full_name → passed as a positional argument
        and captured inside *args.
        """
        first, last = full_name.split(" ")
        self.first_name = first
        self.last_name = last
        print("Name updated successfully")


# ============================================================
#                   USAGE & OUTPUT
# ============================================================

# Creating an Employee object
emp = Employee("Venom", "Shivansh")

# When calling this method:
# emp.show_details()
#
# Internally becomes:
# wrapper(emp)
#
# emp → stored inside *args
emp.show_details()

# When calling this method:
# emp.update_name("Shivansh Yadav")
#
# Internally becomes:
# wrapper(emp, "Shivansh Yadav")
#
# emp, "Shivansh Yadav" → stored inside *args
emp.update_name("Shivansh Yadav")

# Calling again to see updated values
emp.show_details()
