""" Override the len() method on vector of Problem 05 to display the dimension of the Vector """


class Vector:
    """
    Represents an n-dimensional vector.
    """

    def __init__(self, *components):
        # Store all vector components in a list
        self.data = list(components)

    def __len__(self):
        # len(v) calls this method internally
        # Returns the number of components
        return len(self.data)

    def __str__(self):
        # Display the vector neatly
        return f"Vector({', '.join(map(str, self.data))})"



# DEMONSTRATION

# A list of Vector objects with different dimensions
vectors = [
    Vector(1, 2, 3),
    Vector(5, 7),
    Vector(10)
    ]

# Loop through each vector one by one
# This avoids writing separate print statements for every object
for v in vectors:
    # str(v) converts the vector to readable text
    # <15 sets a fixed width for alignment (adjust number for more/less space)
    # len(v) returns the dimension of the vector
    print(f"{str(v):<20} → Dimension: {len(v)}D")

