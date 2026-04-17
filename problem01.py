#1. Create a class (2-D vector) and use it to create another class representing a 3-D 
#vector
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"Vector2D: ({self.x}, {self.y})")
class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def display(self):
        super().display()
        print(f"Vector3D: ({self.x}, {self.y}, {self.z})")
vector3d = Vector3D(1, 2, 3)
vector3d.display()
