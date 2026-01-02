'''
    Create a class Vector and implement the __str__() method to print the vector in the format 
    "5i + 7j + 11k".
'''

class Vector:
    """
    Represents a 3D vector using i, j, and k components.
    """

    def __init__(self, i, j, k):
        # i → x-direction component
        # j → y-direction component
        # k → z-direction component
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        # Controls how the vector is displayed when printed
        return f"{self.i}i + {self.j}j + {self.k}k"


# Creating a Vector object
v = Vector(5, 7, 11)

# Printing the vector automatically calls __str__()
print(v)


