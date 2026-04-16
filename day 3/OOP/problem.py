#Create a class “Programmer” for storing information of few programmers 
#working at Microsoft. 

class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product