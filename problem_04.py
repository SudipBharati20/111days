#Write a program to find whether a given username contains less than 10
#characters or not.

name = input("enter your name: ")

if(len(name) <10 ):
    print("Your name characters are less than 10")
elif(len(name) ==10):
    print("Your name characters are exactly 10")
else:
    print("Yopur name characters are more than 10")