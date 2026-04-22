class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

s = Student("Sudip")
print(s.name)