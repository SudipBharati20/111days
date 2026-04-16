#Can you change the self-parameter inside a class to something else (say 
#“harry”). Try changing self to “slf” or “harry” and see the effects. 
class MyClass:
    def __init__(harry, name):
        harry.name = name
    def display_name(slf):
        print(f"Name: {slf.name}")
obj = MyClass("Alice")
obj.display_name()
