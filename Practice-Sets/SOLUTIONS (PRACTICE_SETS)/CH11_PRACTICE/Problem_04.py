"""
Write a class 'Complex' to represent complex numbers,  along with overloaded operators '+' and '*'
which adds and multiplies them. 
"""

"""
Write a class 'Complex' to represent complex numbers,
with overloaded '+' and '*' operators.
"""

class Complex:
    """
    Represents a complex number in the form:
    a + bi
    """

    def __init__(self, real, imaginary):
        # self → refers to the current object being created
        # real → real part of the complex number
        # imaginary → imaginary part of the complex number
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        # self  → left operand (e.g., c1 in c1 + c2)
        # other → right operand (e.g., c2 in c1 + c2)

        # Ensure the operation is done only with another Complex object
        if not isinstance(other, Complex):
            return NotImplemented

        # (a + bi) + (c + di)
        return Complex(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def __mul__(self, other):
        # self  → first complex number
        # other → second complex number

        # Prevent invalid multiplication with non-Complex types
        if not isinstance(other, Complex):
            return NotImplemented

        # Applying the formula:
        # (a + bi)(c + di) = (ac − bd) + (ad + bc)i
        real_part = (self.real * other.real) - (self.imaginary * other.imaginary)
        imag_part = (self.real * other.imaginary) + (self.imaginary * other.real)

        return Complex(real_part, imag_part)

    def __str__(self):
        # Controls how the object is displayed when printed
        sign = "+" if self.imaginary >= 0 else "-"
        return f"{self.real} {sign} {abs(self.imaginary)}i"


# ============================================================
#                   USER INPUT & EXECUTION
# ============================================================

def read_complex(label):
    # Reads user input and creates a Complex object
    real = float(input(f"Enter Real part of {label}: "))
    imaginary = float(input(f"Enter Imaginary part of {label}: "))
    return Complex(real, imaginary)


# Code below runs only when the file is executed directly
if __name__ == "__main__":
    print("\n================== Complex Number Calculator (Addition & Multiplication) ==================\n")

    c1 = read_complex("Complex No.01")
    c2 = read_complex("Complex No.02")

    print("\nResults:")
    print(f"Complex No.01 : {c1}")
    print(f"Complex No.02 : {c2}")
    print(f"Sum           : {c1 + c2}")
    print(f"Product       : {c1 * c2}")
