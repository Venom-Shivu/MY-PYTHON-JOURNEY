# ============================================================
#                OPERATOR OVERLOADING IN PYTHON
# ============================================================

"""
OPERATOR OVERLOADING:
--------------------
Python allows us to define how operators behave with
user-defined objects using special methods
called dunder (double underscore) methods.

Example:
+   → __add__()
-   → __sub__()
*   → __mul__()
/   → __truediv__()
%   → __mod__()
len() → __len__()
str() → __str__()
"""

class Number:
    def __init__(self, n):
        # Store the numeric value inside the object
        self.n = n

    # --------------------------------------------------------
    # ADDITION (+)
    # --------------------------------------------------------
    def __add__(self, other):
        # Called when: obj1 + obj2
        return self.n + other.n

    # --------------------------------------------------------
    # SUBTRACTION (-)
    # --------------------------------------------------------
    def __sub__(self, other):
        # Called when: obj1 - obj2
        return self.n - other.n

    # --------------------------------------------------------
    # MULTIPLICATION (*)
    # --------------------------------------------------------
    def __mul__(self, other):
        # Called when: obj1 * obj2
        return self.n * other.n

    # --------------------------------------------------------
    # TRUE DIVISION (/) Returns the Quotient (How many times one number fits into another)
    # --------------------------------------------------------
    def __truediv__(self, other):
        # Called when: obj1 / obj2
        return self.n / other.n

    # --------------------------------------------------------
    # MODULUS (%) Returns the remainder
    # --------------------------------------------------------
    def __mod__(self, other):
        # Called when: obj1 % obj2
        return self.n % other.n

    # --------------------------------------------------------
    # STRING REPRESENTATION
    # --------------------------------------------------------
    def __str__(self):
        """
        Called when:
        - print(obj)
        - str(obj)

        Controls how the object is displayed.
        """
        return f"Number({self.n})"

    # --------------------------------------------------------
    # LENGTH REPRESENTATION
    # --------------------------------------------------------
    def __len__(self):
        """
        Called when:
        - len(obj)

        Here, we define length as the number of digits.
        """
        return len(str(self.n))


# ============================================================
#                   USAGE & DEMONSTRATION
# ============================================================

n = Number(10)
m = Number(3)

# Arithmetic operations
print(f"="*20, "Arithmetic Operations", "="*20)
print("Addition        :", n + m)   # Calls __add__
print("Subtraction     :", n - m)   # Calls __sub__
print("Multiplication  :", n * m)   # Calls __mul__
print("Division        :", n / m)   # Calls __truediv__
print("Modulus         :", n % m)   # Calls __mod__

# String representation
print(f"\n" + "="*20, "String Representation", "="*20)    
print(n)                          # print(obj) automatically calls obj.__str__(),
print(str(n))                     # so print(obj) and print(str(obj)) behave exactly the same.

# Length representation
print(f"\n" + "="*20, "Length Representation", "="*20)
print(len(n))                       # Calls __len__
