"""     Can You change the self-parameter inside a class to something else (say "venom").
                Try Changing self to "slf" or "venom" and see what happens.                   """

class DemoVenom:
    # Using 'venom' instead of 'self'
    def __init__(venom, name):
        venom.name = name

    def greet(venom):
        print(f"[Venom] Hello {venom.name}! Method works without using 'self'.")


class DemoSlf:
    # Using 'slf' instead of 'self'
    def __init__(slf, name):
        slf.name = name

    def greet(slf):
        print(f"[Slf] Hello {slf.name}! Method works without using 'self'.")


# --------------------------------------------------
# Object Creation & Method Calls
# --------------------------------------------------

obj1 = DemoVenom("Shivansh")
obj2 = DemoSlf("Shivansh")

obj1.greet()
obj2.greet()


"""
CONCLUSION:
- 'self' is NOT a keyword in Python.
- Any valid identifier can replace it (e.g., venom, slf).
- Python passes the instance as the first argument automatically.
- This works ONLY for instance method calls (obj.method()).
- In real-world and industry code, ALWAYS use 'self'.
  Using anything else hurts readability and will fail code reviews.
"""
