# File: table_7_vertical.py

# Q3: A list contains multiplication table of 7.
# Convert it into vertical string.

table = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# Convert list to vertical format
vertical_output = "\n".join(str(i) for i in table)

print(vertical_output)