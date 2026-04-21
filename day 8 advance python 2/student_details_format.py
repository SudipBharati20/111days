# File: student_details_format.py

# Q2: Write a program to input name, marks and phone number of a student and format it.

name = input("Enter name: ")
marks = int(input("Enter marks: "))
phone = input("Enter phone number: ")

# Using format() function
result = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)

print(result)