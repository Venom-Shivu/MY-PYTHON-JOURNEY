# Create a class (2-D vecotr) and use it to create another class representing a 3-D vector.

# ============================================================
#          2-D VECTOR AND 3-D VECTOR USING INHERITANCE
# ============================================================

class Vector2D:
    """
    Represents a 2-D vector in the form:
    ai + bj
    """

    def __init__(self, i, j):
        # Initialize x and y components of the vector
        self.i = i
        self.j = j

    def __str__(self):
        # String representation of a 2-D vector
        return f"{self.i}i + {self.j}j"


class Vector3D(Vector2D):
    """
    Represents a 3-D vector by extending a 2-D vector.
    Inherits i and j from Vector2D and adds k.
    """

    def __init__(self, i, j, k):
        # Initialize i and j using the parent class constructor
        super().__init__(i, j)

        # Initialize z component of the vector
        self.k = k

    def __str__(self):
        # String representation of a 3-D vector
        return f"{self.i}i + {self.j}j + {self.k}k"


# ============================================================
# OBJECT CREATION & OUTPUT
# ============================================================

v2 = Vector2D(1, 2)
v3 = Vector3D(1, 2, 3)
print("-----------2-D & 3-D Vectors-----------")
print(f"2-D Vector: {v2}")
print(f"3-D Vector: {v3}")


# ============================================================
#           NUMPY-STYLE VECTORS USING INHERITANCE
# ============================================================

class Vector2D:
    """
    Represents a 2-D vector similar to NumPy array style.
    Example output: [1 2]
    """

    def __init__(self, x, y):
        # Store vector components in a list (NumPy-like)
        self.data = [x, y]

    def __str__(self):
        # NumPy-style string representation
        return f"[{self.data[0]} {self.data[1]}]"

    def __repr__(self):
        # Official representation (used in console/debugging)
        return f"Vector2D({self.data})"


class Vector3D(Vector2D):
    """
    Represents a 3-D vector extending a 2-D vector.
    Example output: [1 2 3]
    """

    def __init__(self, x, y, z):
        # Initialize x and y using parent class
        super().__init__(x, y)

        # Add z component
        self.data.append(z)

    def __str__(self):
        # NumPy-style string representation
        return f"[{self.data[0]} {self.data[1]} {self.data[2]}]"

    def __repr__(self):
        return f"Vector3D({self.data})"


# ============================================================
# OBJECT CREATION & OUTPUT
# ============================================================

v2 = Vector2D(1, 2)
v3 = Vector3D(1, 2, 3)
print("-----------NumPY Style Vectors-----------")
print("2-D Vector:", v2)
print("3-D Vector:", v3)

