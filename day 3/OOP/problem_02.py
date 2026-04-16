#Create a class with a class attribute a; create an object from it and set ‘a’ 
#directly using ‘object.a = 0’. Does this change the class attribute?

class MyClass:
    a = 10
obj = MyClass()
print(MyClass.a)  # Output: 10
obj.a = 0
print(MyClass.a)  # Output: 10
print(obj.a)      # Output: 0

