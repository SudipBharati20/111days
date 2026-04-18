#ENumerate keyword
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

# Using enumerate with a custom start index
for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")

