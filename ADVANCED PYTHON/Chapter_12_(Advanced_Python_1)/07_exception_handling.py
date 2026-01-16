"""
=================================================
        EXCEPTION HANDLING IN PYTHON
=================================================

Exception handling allows a program to respond to
runtime errors gracefully instead of crashing.

Core keywords:
- try      : Code that may raise an exception
- except   : Handles specific exceptions
- else     : Runs only if no exception occurs
- finally  : Always runs (cleanup, logging, etc.)
"""

print("\n========== EXAMPLE 1 : ValueError ==========")

# ------------------------------------------------
# ValueError
# Raised when the value is invalid for the given type
# ------------------------------------------------

try:
    age = int(input("Enter your age: "))
    print("OUTPUT -> Age entered:", age)

except ValueError:
    print("OUTPUT -> ValueError: Please enter a numeric value.")


print("\n========== EXAMPLE 2 : TypeError ==========")

# ------------------------------------------------
# TypeError
# Raised when incompatible data types are used together
# ------------------------------------------------

try:
    result = 10 + "5"
    print("OUTPUT -> Result:", result)

except TypeError:
    print("OUTPUT -> TypeError: Cannot add int and string.")


print("\n========== EXAMPLE 3 : IndexError ==========")

# ------------------------------------------------
# IndexError
# Raised when accessing an invalid list index
# ------------------------------------------------

numbers = [10, 20, 30]

try:
    print("OUTPUT -> Element:", numbers[5])

except IndexError:
    print("OUTPUT -> IndexError: List index out of range.")


print("\n========== EXAMPLE 4 : KeyError ==========")

# ------------------------------------------------
# KeyError
# Raised when a dictionary key does not exist
# ------------------------------------------------

student = {"name": "Shivu", "age": 22}

try:
    print("OUTPUT -> Grade:", student["grade"])

except KeyError:
    print("OUTPUT -> KeyError: Dictionary key not found.")


print("\n========== EXAMPLE 5 : Multiple Exceptions ==========")

# ------------------------------------------------
# Handling multiple exceptions
# ------------------------------------------------

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("OUTPUT -> Division Result:", a / b)

except ValueError:
    print("OUTPUT -> ValueError: Numeric input required.")

except ZeroDivisionError:
    print("OUTPUT -> ZeroDivisionError: Division by zero not allowed.")


print("\n========== EXAMPLE 6 : else & finally ==========")

# ------------------------------------------------
# try + except + else + finally
# ------------------------------------------------

try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("OUTPUT -> ValueError: Invalid input.")

except ZeroDivisionError:
    print("OUTPUT -> ZeroDivisionError: Cannot divide by zero.")

else:
    print("OUTPUT -> Calculation successful:", result)

finally:
    print("OUTPUT -> Execution completed.")


print("\n========== EXAMPLE 7 : User Defined Exception ==========")

# ------------------------------------------------
# Custom (user-defined) exception
# ------------------------------------------------

class NegativeNumberError(Exception):
    """Raised when a negative number is provided"""
    pass


try:
    number = int(input("Enter a positive number: "))

    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")

    print("OUTPUT -> Valid number:", number)

except NegativeNumberError as error:
    print("OUTPUT -> CustomError:", error)

except ValueError:
    print("OUTPUT -> ValueError: Please enter a valid integer.")


print("\n========== EXAMPLE 8 : Raising ValueError Manually ==========")

# ------------------------------------------------
# Raising ValueError explicitly
# Used when input violates a logical/business rule
# ------------------------------------------------

try:
    marks = int(input("Enter your marks (0 - 100): "))

    # Logical validation (not a type issue)
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100.")

    print("OUTPUT -> Valid marks entered:", marks)

except ValueError as error:
    # Handles both conversion errors and manually raised ValueError
    print("OUTPUT -> ValueError:", error)


print("\n========== EXAMPLE 9 : Assertions ==========")

# ------------------------------------------------
# Assertions
# Used for internal consistency checks during development.
# NOT meant for user input validation.
# Can be disabled with Python -O optimization flag.
# ------------------------------------------------

def calculate_discount(price, discount_percentage):
    assert 0 <= discount_percentage <= 100, \
        "Discount percentage must be between 0 and 100."
    return price * (1 - discount_percentage / 100)


# Valid case
print("OUTPUT -> Discounted price (20%):",
      calculate_discount(100, 20))


# Invalid case (handled to avoid crashing the script)
try:
    print("OUTPUT -> Discounted price (120%):",
          calculate_discount(100, 120))

except AssertionError as error:
    print("OUTPUT -> AssertionError:", error)
