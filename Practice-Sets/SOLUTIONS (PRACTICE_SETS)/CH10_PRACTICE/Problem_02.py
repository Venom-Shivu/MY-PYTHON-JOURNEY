# Write a class "calculator" capable of finding square, cube, and square root of a number entered by user

class Calculator:
    """
    A utility class that provides basic mathematical operations.
    This class does not store state; it only performs calculations.
    """
    @staticmethod #@staticmethod clearly says: “This method does not depend on object or class state.”
    def square(number):
        """
        Returns the square of the given number.
        """
        return number ** 2

    @staticmethod
    def cube(number):
        """
        Returns the cube of the given number.
        """
        return number ** 3

    @staticmethod 
    def square_root(number):
        """
        Returns the square root of the given number.
        Raises an error for negative inputs.
        """
        if number < 0:
            raise ValueError("Square root of a negative number is not defined for real numbers.")
        return number ** 0.5


# ============================================================
# User Input & Execution
# ============================================================

try:
    # Handles runtime errors caused by invalid user input or invalid calculations,
    # preventing the program from crashing.

    # Taking numeric input from the user
    num = float(input("Enter a number: "))

    # Performing calculations using the Calculator class
    print(f"Square      : {Calculator.square(num)}")
    print(f"Cube        : {Calculator.cube(num)}")
    print(f"Square Root : {Calculator.square_root(num)}")

except ValueError as error:
    # Handles invalid input or invalid mathematical operations
    print("Error:", error)
