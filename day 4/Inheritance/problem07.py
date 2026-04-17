#7. Override the __len__() method on vector of problem 5 to display the dimension of the 
#vector.
class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __len__(self):
        return len(self.components)

    def display(self):
        print(f"Vector: {self.components}")
vector1 = Vector([1, 2, 3])
print(f"Dimension of vector1: {len(vector1)}")  # Output: Dimension of vector1: 3
vector2 = Vector([4, 5, 6, 7])
print(f"Dimension of vector2: {len(vector2)}")  # Output: Dimension of vector2: 4
vector_sum = vector1 + Vector([7, 8, 9])  # This will work
vector_sum.display()  # Output: Vector: [8, 10, 12]
# The following line will raise an error due to dimension mismatch
# vector_sum = vector1 + vector2  # Uncommenting this will raise ValueError: Vectors must have the same dimensions for addition.
