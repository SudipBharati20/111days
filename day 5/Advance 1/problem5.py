'''
5. Store the multiplication tables generated in problem 3 
in a file named Tables.txt.
'''

num = int(input("Enter number for the table: "))
table = [num * i for i in range(1, 11)]

# 'a' mode appends to the file so you don't lose previous tables
with open("Tables.txt", "a") as f:
    f.write(f"Table of {num}: {str(table)}\n")
    
print("Table has been saved to Tables.txt")