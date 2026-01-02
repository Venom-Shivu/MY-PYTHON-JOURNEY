""" 
Write a class Vector representing a Vector of n dimensions. Overload the '+' and '*' operator
which calculates the sum and dot(.) product of them.
"""

class Vector:
    """
    Represents an n-dimensional mathematical vector.
    Example: Vector(1, 2, 3)
    """

    def __init__(self, *components):
        # self → current object being created
        # *components → collects multiple values into a tuple
        # Example: Vector(1, 2, 3) → components = (1, 2, 3)
        self.data = list(components)

    def __add__(self, other):
        # '+' operator calls this method: v1 + v2
        # self  → v1
        # other → v2

        # Ensure addition is done only between Vector objects
        if not isinstance(other, Vector):
            return NotImplemented
        #Tells Python: “I don’t know how to handle this type”
        #Allows Python to try reverse operations or raise proper errors
        
        # Both vectors must have same number of dimensions
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must have the same dimensions.")

        # zip() pairs elements from both vectors
        # Example:
        # zip([1,2,3], [4,5,6]) → (1,4), (2,5), (3,6)
        result = [
            a + b for a, b in zip(self.data, other.data)
        ]

        # *result unpacks the list into separate arguments
        # Vector(*[5,7,9]) → Vector(5, 7, 9)
        return Vector(*result)

    def __mul__(self, other):
        # '*' operator calls this method: v1 * v2
        # Performs DOT PRODUCT (returns a number, not a vector)

        if not isinstance(other, Vector):
            return NotImplemented

        if len(self.data) != len(other.data):
            raise ValueError("Vectors must have the same dimensions.")

        # zip() pairs corresponding components
        # a*b multiplies each pair
        # sum() adds all products together
        # Example:
        # (1*4) + (2*5) + (3*6)
        return sum(a * b for a, b in zip(self.data, other.data))

    def __str__(self):
        # map(str, self.data) converts each number to string
        # Example: [1,2,3] → ["1","2","3"]
        # join() combines them with ", "
        return f"Vector({', '.join(map(str, self.data))})"


# ============================================================
#                   USAGE & DEMONSTRATION
# ============================================================

if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print("Vector 1 :", v1)
    print("Vector 2 :", v2)
    print("Sum      :", v1 + v2)
    print("Dot Prod :", v1 * v2)
