"""
SAVE TABLE TO FILE
"""

n = int(input("Enter number: "))

table = [n*i for i in range(1,11)]

with open("Tables.txt", "w") as f:
    for val in table:
        f.write(str(val) + "\n")

print("Saved successfully")