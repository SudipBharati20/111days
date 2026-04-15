#conditional Expression

a = 3
if (a>3):
    print("The value of a is grater")
elif(a>7):
    print("The value of a is greater than 7")
else:
    print("It is higher than value of a")


#conditional expression quiz
#Write a program to print yes
# when the age entered by the user is greater than or equal to 18.

Age = int(input("Enter your age: "))
if Age <= 18:
    print("child")
elif(Age >= 80):
    print("senior")