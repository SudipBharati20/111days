'''
3. Write a list comprehension to print a list which contains 
the multiplication table of a user entered number. 
'''

num = int(input("Enter a number: "))

# One-liner to generate the table from 1 to 10
table = [num * i for i in range(1, 11)]

print(f"Table for {num}: {table}")