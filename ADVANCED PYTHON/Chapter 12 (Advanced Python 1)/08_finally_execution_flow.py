"""
=================================================
        UNDERSTANDING `finally` IN PYTHON
=================================================

This file demonstrates:
1. Why code after `return` does NOT run
2. Why `finally` ALWAYS runs
3. How `finally` behaves with exceptions
"""

print("\n========== CASE 1 : print AFTER return (NO finally) ==========")

def case_without_finally():
    try:
        print("Inside try block")
        return "Returning from function"
        # Any code after return is unreachable
        print("This line will NEVER execute")

    except Exception:
        print("Inside except block")


result = case_without_finally()
print("OUTPUT -> Function returned:", result)


print("\n========== CASE 2 : print inside finally ==========")

def case_with_finally():
    try:
        print("Inside try block")
        return "Returning from function"

    finally:
        # This ALWAYS executes before function exits
        print("Inside finally block (always executed)")


result = case_with_finally()
print("OUTPUT -> Function returned:", result)


print("\n========== CASE 3 : Exception without finally ==========")

def exception_without_finally():
    try:
        print("Inside try block")
        10 / 0  # Raises ZeroDivisionError
        print("This will NOT execute")

    except ZeroDivisionError:
        return "Exception handled, function returning"


result = exception_without_finally()
print("OUTPUT -> Function returned:", result)


print("\n========== CASE 4 : Exception with finally ==========")

def exception_with_finally():
    try:
        print("Inside try block")
        10 / 0

    except ZeroDivisionError:
        return "Exception handled, function returning"

    finally:
        # Guaranteed execution even after exception + return
        print("Inside finally block (cleanup guaranteed)")


result = exception_with_finally()
print("OUTPUT -> Function returned:", result)


print("\n========== FINAL CONCLUSION ==========")
print(
    "Code after return or exception does NOT run.\n"
    "`finally` ALWAYS runs before function exits."
)
