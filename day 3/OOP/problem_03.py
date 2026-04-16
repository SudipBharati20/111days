#Add a static method in problem 2, to greet the user with hello. 
class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product

    @staticmethod
    def greet():
        print("Hello!")
programmer1 = Programmer("Alice", "Windows")
programmer2 = Programmer("Bob", "Office")   
programmer1.greet()
programmer2.greet() 
