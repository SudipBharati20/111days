#2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
#‘Pets’. Add a method ‘bark’ to class ‘Dog’.
class Animals:
    def __init__(self, species):
        self.species = species

    def display_species(self):
        print(f"Species: {self.species}")
class Pets(Animals):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name

    def display_name(self):
        print(f"Pet Name: {self.name}")
class Dog(Pets):
    def __init__(self, species, name, breed):
        super().__init__(species, name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")
dog = Dog("Canine", "Buddy", "Golden Retriever")
dog.display_species()
dog.display_name()
dog.bark()
