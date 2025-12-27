# ============================================================
#            PROPERTY DECORATORS (GETTERS / SETTERS)
# ============================================================
"""
WHAT ARE PROPERTY DECORATORS?
-----------------------------
Property decorators allow a method to behave like an attribute.

Why they exist:
1. Control access to internal data (encapsulation)
2. Validate data before assigning it
3. Compute values dynamically instead of storing them

Decorators used:
- @property        → getter  (read-only access)
- @property_name.setter  → setter (controlled write access)
- @property_name.deleter → deleter (controlled delete access)
"""

class Employee:
    def __init__(self, first_name, last_name):
        # Internal attributes (should not be accessed directly)
        self._first = first_name
        self._last = last_name

    # --------------------------------------------------------
    # GETTER
    # --------------------------------------------------------
    @property
    def email(self):
        """
        Acts like a normal variable: emp.email
        Email is generated dynamically from first and last name.
        """
        if self._first is None or self._last is None:
            return "Email not available"
        return f"{self._first.lower()}.{self._last.lower()}@company.com"

    # --------------------------------------------------------
    # SETTER
    # --------------------------------------------------------
    @email.setter
    def email(self, value):
        """
        Allows setting email like:
        emp.email = "john.doe@company.com"

        Validates format and updates first and last name.
        """
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email format")

        print(f">> Updating email to: {value}")

        name_part = value.split("@")[0]
        first, last = name_part.split(".")

        self._first = first.capitalize()
        self._last = last.capitalize()

    # --------------------------------------------------------
    # DELETER
    # --------------------------------------------------------
    @email.deleter
    def email(self):
        """
        Allows deletion using:
        del emp.email

        Resets related internal data safely.
        """
        print(">> Deleting email and clearing names")
        self._first = None
        self._last = None


# ============================================================
#                   USAGE & DEMONSTRATION
# ============================================================

emp = Employee("Shivansh", "Yadav")

# Getter works like an attribute
print(f"Initial Email : {emp.email}")

# Setter updates internal state safely
emp.email = "venom.coding@company.com"
print(f"Updated Email : {emp.email}")

# Accessing internal data (still available)
print(f"First Name    : {emp._first}")
print(f"Last Name     : {emp._last}")

# Deleter resets the data
del emp.email
print(f"After Delete  : {emp.email}")
