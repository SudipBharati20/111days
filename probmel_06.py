#Write a program to calculate the grade of a student from his marks from the
#following scheme:
#90 - 100 => Ex
#80 - 90 => A
#70 - 80 => B
#60 - 70 =>C
#50 - 60 => D
#<50 => F

Marks = int(input("Enter your marks: "))

if Marks> 90:
    print("excellent")
elif Marks>80:
    print("A")
elif Marks>70:
    print("B")
elif Marks>60:
    print("c")
elif Marks>50:
    print("D")
elif Marks>40:
    print("E")
else:
    print("Fail")
